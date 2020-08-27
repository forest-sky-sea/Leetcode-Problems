from collections import deque
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []
        queue = deque()
        find_num = []
        for i, num in enumerate(nums):
            if num not in find_num:
                queue.append(([num], i))
                find_num.append(num)
        res = []

        while queue:
            cur_num, cur_i = queue.popleft()
            find_num = []
            for j in range(cur_i + 1, len(nums)):
                if nums[j] >= nums[cur_i]:
                    if nums[j] not in find_num:
                        app_num = cur_num + [nums[j]]
                        res.append(app_num)
                        queue.append((app_num, j))
                        find_num.append(nums[j])

        return res


print(Solution().findSubsequences([5, 4, 7, 7]))
print(Solution().findSubsequences([4, 6, 7, 7]))
