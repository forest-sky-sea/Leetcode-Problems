from typing import List


class Solution:
    # 52ms
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 1
        last = ''
        while i >= 0:
            if nums[i] == last:
                nums.pop(i)
            else:
                last = nums[i]
            i -= 1
        return len(nums)

    # guided 48ms
    def removeDuplicates1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j = 0, 1
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                if j - i > 0:
                    nums[i] = nums[j]
        return i + 1


l = [1,1,2,3,4,5,6,6,6,7,7,7]
print(Solution().removeDuplicates1(l))
print(l)
