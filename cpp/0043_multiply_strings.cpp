class Solution {
public:
    string multiply(string num1, string num2) {
      if (num1 == "0" || num2 == "0")
        return "0";
      if (num1 == "1") {
        return num2;
      } else if (num2 == "1") {
        return num1;
      }

      int len1 = num1.length();
      int len2 = num2.length();
      int len_res = len1 + len2;

      string res(len_res, '0');

      int carry = 0;

      for (int i = 0 ; i < len2; i++) {
        for (int j = 0; j < len1; j++) {
          int temp = (num2[len2-1-i] - '0') * (num1[len1-1-j] - '0') + (res[len_res - 1 - i - j] - '0')  + carry;
          res[len_res - 1 - i - j] = temp%10 + '0';
          carry = temp/10; 
        }
        if(carry != 0) {
            res[len_res -1 - i - len1] = carry + '0';
            carry = 0;
        }
      }
      
      res.erase(0,res.find_first_not_of("0"));
      return res;
    }
};
