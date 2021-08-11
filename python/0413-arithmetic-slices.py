from typing import List


class Solution:
    def numberOfArithmeticSlices1(self, nums: List[int]) -> int:
        n = len(nums)
        arith_len = [0] * n
        i = n - 3
        cond = 0

        def is_arithmetic(a: int, b: int, c: int):
            if c - b == b - a:
                return True
            else:
                return False

        while i >= 0:
            if is_arithmetic(nums[i], nums[i + 1], nums[i + 2]):
                arith_len[i] = arith_len[i + 1] + 1 + cond
                cond += 1
            else:
                arith_len[i] = arith_len[i + 1]
                cond = 0
            i -= 1
        return arith_len[0]

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        diff = nums[n - 2] - nums[n - 1]
        add_count = 0
        res = 0
        i = n - 3
        while i >= 0:
            if nums[i] - nums[i + 1] == diff:
                add_count += 1
            else:
                diff = nums[i] - nums[i + 1]
                add_count = 0
            res += add_count
            i -= 1
        return res


print(Solution().numberOfArithmeticSlices([1, 2, 3, 4, 5, 7, 8, 9]))
