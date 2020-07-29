class Solution {
public:
    string longestPalindrome(string s) {
        if (s == "" || s.length() == 1)
            return s;
        int max_length = 0;
        string res;

        for (int i = 0; i < s.length(); i++) {
            int begin = i;
            while ((i+1) < s.length() && s[i+1] == s[i]) {
                i++;
            }
            int len = 0;
            // int right = 1;
            while ((begin-len-1)>=0 && (i+len+1) < s.length() && s[begin-len-1] == s[i+len+1]) {
                len ++;
            }
            if ((i-begin+1+len*2) > max_length) {
                max_length = i-begin+1+len*2;
                res = s.substr((begin-len), max_length);
            }  

        }

        return res;
    }
};
