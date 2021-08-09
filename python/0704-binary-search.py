from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        return -1


# print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
print(Solution().search([5], 5))
