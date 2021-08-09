from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        i, j = 0, len(nums) - 1
        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                res.append(nums[i] * nums[i])
                i += 1
            else:
                res.append(nums[j] * nums[j])
                j -= 1
        return res[::-1]


print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
