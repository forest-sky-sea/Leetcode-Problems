class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        l = len(s)
        for i, c in enumerate(s):
            left, right = i, i
            while left >= 0 and right < l and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            left, right = i, i + 1
            while left >= 0 and right < l and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

    def countSubstrings2(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        pos = {}
        for i, c in enumerate(s):
            if c not in pos.keys():
                pos[c] = [i]
            else:
                for prev in pos[c]:
                    if s[prev: i + 1] == s[prev: i + 1][::-1]:
                        res += 1
                pos[c].append(i)
        return res + len(s)


print(Solution().countSubstrings('abacadda'))
print(Solution().countSubstrings('abc'))
print(Solution().countSubstrings('aaa'))
