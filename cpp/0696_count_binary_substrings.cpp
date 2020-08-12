class Solution {
public:
    int countBinarySubstrings(string s) { 
        if (s.length() < 2)
          return 0;
        
        char cur = s[0];
        int last = 0;
        int res = 0;
        int tmp_cnt = 0;
      
        for(int i = 0 ; i < s.length(); i++) {
          while(s[i] == cur && i < s.length()) {
            tmp_cnt++;
            i++;
          }
          // cout << i << ") " << last << " " << tmp_cnt << endl; 
          res += min(last, tmp_cnt);
          cur = s[i];
          last = tmp_cnt;
          i--;
          tmp_cnt = 0;
        }

        return res;
    }
};
