from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        s_sub = []

        def dfs(s):
            if len(s_sub) == k:
                res.append(s_sub.copy())
                return
            for i in range(s, n - (k - len(s_sub) - 2)):
                s_sub.append(i)
                dfs(i + 1)
                s_sub.pop(-1)

        dfs(1)

        return res


a = Solution().combine(5, 3)
b = 0
