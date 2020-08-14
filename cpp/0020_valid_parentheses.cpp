class Solution {
public:
    bool isValid(string s) {
        if (s == "") 
            return true;
        if (s.length() % 2 == 1)
            return false;
        stack<char>kuohao;
        for (int i = 0 ; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                kuohao.push(s[i]);
            } else {
                if (kuohao.empty()) {
                    return false;
                }  else if (s[i] == ')' && kuohao.top() == '(') {
                    kuohao.pop();
                } else if (s[i] == '}' && kuohao.top() == '{') {
                    kuohao.pop();
                } else if (s[i] == ']' && kuohao.top() == '[') {
                    kuohao.pop();
                } else {
                    return false;
                }
               
            }
        }
        if (kuohao.empty())
            return true;
        else
            return false;
    }
};
