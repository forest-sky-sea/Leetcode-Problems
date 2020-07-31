from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i == num:
                return num
        return -1

    # for Increasing positive list
    def findMagicIndex1(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == nums[i]:
                return i
            i = nums[i]
        return -1

    # for Strictly monotonically increasing list (nlog(n))
    def findMagicIndex2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                return mid
            if nums[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
        return -1


Solution().findMagicIndex1([1, 4, 4, 4, 6, 8, 9, 9, 9, 9, 13, 14, 15, 16, 17, 18])
Solution().findMagicIndex2([-10, -9, -8, -7, 0, 1, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
# https://leetcode-cn.com/problems/magic-index-lcci/
