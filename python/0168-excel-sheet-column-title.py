class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber > 0:
            columnNumber -= 1
            cat = columnNumber % 26
            res += (chr(cat + ord('A')))
            columnNumber //= 26
        return res[::-1]


print(Solution().convertToTitle(28))
