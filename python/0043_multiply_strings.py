from typing import List


class Solution:
    def add(self, nums: List[str]) -> str:
        i, carry = 0, 0
        res = ''
        breakable = False
        while True:
            sub_sum = 0
            for j, num in enumerate(nums):
                if len(num) > i >= j:
                    sub_sum += int(num[i])
                    breakable = False
            if breakable:
                if carry != 0:
                    res += str(carry)
                break
            else:
                sub_sum += carry
                carry = sub_sum // 10
                sub_sum = sub_sum % 10
                res += str(sub_sum)
                i += 1
                breakable = True
        return res[::-1]

    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        if len1 == 0 or len2 == 0:
            return '0'
        if num1 == '0' or num2 == '0':
            return '0'
        if len2 > len1:
            tmp = num1
            num1 = num2
            num2 = tmp
            tmp = len1
            len1 = len2
            len2 = tmp
        res = []
        dp_cache = ['' for _ in range(10)]
        dp_cache[1] = num2[::-1]
        i = len1 - 1
        while i >= 0:
            if num1[i] != '0':
                if dp_cache[int(num1[i])]:
                    sub_res = dp_cache[int(num1[i])]
                else:
                    j = len2 - 1
                    sub_carry = 0
                    sub_res = ''
                    while j >= 0:
                        sub_sum = int(num1[i]) * int(num2[j]) + sub_carry
                        sub_carry = sub_sum // 10
                        sub_sum = sub_sum % 10
                        sub_res += str(sub_sum)
                        j -= 1
                    if sub_carry != 0:
                        sub_res += str(sub_carry)
                    dp_cache[int(num1[i])] = sub_res
                sub_res = '0' * (len1 - 1 - i) + sub_res
                res.append(sub_res)
            i -= 1
        return self.add(res)


print(Solution().multiply('9133', '101'))
print(Solution().multiply('9', '99'))
print(Solution().multiply('9133', '0'))
print(Solution().multiply('2106', '423'))
