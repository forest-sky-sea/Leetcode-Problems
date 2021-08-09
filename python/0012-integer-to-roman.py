class Solution:
    def intToRoman(self, num: int) -> str:
        alphabet = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M'], ['M', 'M', 'M']]
        res = []
        i = 0
        while num > 0:
            c = num % 10
            if c == 4:
                res.insert(0, f'{alphabet[i][0]}{alphabet[i][1]}')
            elif c == 9:
                res.insert(0, f'{alphabet[i][0]}{alphabet[i][2]}')
            else:
                res.insert(0, alphabet[i][0] * (c % 5))
                v = c // 5
                if v == 1:
                    res.insert(0, alphabet[i][1])
            num = num // 10
            i += 1
        return ''.join(res)


print(Solution().intToRoman(1894))
