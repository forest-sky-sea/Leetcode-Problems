class Solution:
    # magic
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return True
        len_s = len(s) * 2
        return (s + s).find(s, 1, len_s - 1) != -1

    def repeatedSubstringPattern2(self, s: str) -> bool:
        if not s:
            return True
        len_s = len(s)
        for i in range(1, len_s // 2 + 1):
            if len_s % i == 0:
                sub = s[0: i]
                j = i
                while j < len_s:
                    if sub != s[j: j + i]:
                        break
                    j += i
                if j == len_s:
                    return True
        return False


print(Solution().repeatedSubstringPattern("abaababaab"))
print(Solution().repeatedSubstringPattern("abacababacab"))
print(Solution().repeatedSubstringPattern('aabcaab'))
print(Solution().repeatedSubstringPattern('aabcaabcdaabcaabcd'))
print(Solution().repeatedSubstringPattern('abcabcabc'))
