class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s == "") {
            return 0;
        }

        if (s.length() == 1) {
            return 1;
        }

        unordered_map<char, int> dic;
        dic[s[0]] = 0;
        int min = 0;
        int max = 0;
        int result = 1;
        for(int i = 1; i<s.length(); i++) {
            auto it = dic.find(s[i]);
            if (it == dic.end()) {
                dic[s[i]] = i;
            } else {
                // found
                if ((max - min + 1) > result) {
                    result = max -min +1;
                }
                if ((dic[(s[i])] + 1) > min)
                    min = dic[(s[i])] + 1;
                dic[(s[i])] = i;
            }
            max = i;
        }
        if ((max - min + 1) > result) {
            result = max -min+1;
        }
        return result;
    }
};
