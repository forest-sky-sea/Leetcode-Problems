class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res_str = ''
        while i >= 0 or j >= 0:
            sum_int = 0
            if i >= 0:
                sum_int += int(num1[i])
            if j >= 0:
                sum_int += int(num2[j])
            sum_int += carry
            if sum_int >= 10:
                carry = 1
                sum_int = sum_int - 10
            else:
                carry = 0
            res_str += str(sum_int)
            i -= 1
            j -= 1
        if carry:
            res_str += '1'

        return res_str[::-1]


print(Solution().addStrings('1999', '1'))
print(Solution().addStrings('2319082', '12314'))
