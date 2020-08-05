class Solution {
public:
    string addStrings(string num1, string num2) {
      if (num1.length() > num2.length()) {
        return addStrings(num2, num1);
      }
      int len1 = num1.length();
      int len2 = num2.length();

      bool flag = false;
      int temp = 0;
      for(int i = 0; i < len2; i++) {
        if (i < len1) {
          temp = num1[len1-1-i] + num2[len2-1-i] - '0'*2 + flag;
        } else {
          temp = num2[len2-1-i] - '0' + flag;
        }
        flag = temp > 9;
        num2[len2-1-i] = temp % 10 + '0';
      }
      if (flag) {
        return '1'+num2;
      } else {
        return num2;
      }
    }
};
