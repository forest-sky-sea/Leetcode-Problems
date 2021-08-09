from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(start: int, end: int, k: int):
            if start > end:
                return -1
            while start < end:
                mid = start + (end - start) // 2
                if k <= nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            return start

        left_index = binary_search(0, len(nums) - 1, target)
        if left_index == -1 or nums[left_index] != target:
            return [-1, -1]
        right_index = binary_search(0, len(nums) - 1, target + 1)
        if right_index == len(nums) - 1 and nums[right_index] == target:
            return [left_index, right_index]
        return [left_index, right_index - 1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 7))
