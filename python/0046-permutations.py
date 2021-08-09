from typing import List
from collections import deque


class Solution:
    # def permute1(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) == 1:
    #         return [nums]
    #     else:
    #         res = []
    #         for n in nums:
    #             remain = nums.copy()
    #             remain.remove(n)
    #             tmp = self.permute(remain)
    #             for t in tmp:
    #                 t.insert(0, n)
    #             res.extend(tmp)
    #         return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []

        def dfs(depth: int, path: deque[int], used: List[bool]):
            if depth == length:
                res.append(list(path.copy()))
            else:
                for i, num in enumerate(nums):
                    if not used[i]:
                        path.append(nums[i])
                        used[i] = True
                        dfs(depth + 1, path, used)
                        used[i] = False
                        path.pop()

        dfs(0, deque(), [False for _ in range(length)])
        return res


print(Solution().permute([1, 2, 3]))
