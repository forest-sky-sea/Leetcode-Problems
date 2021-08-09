from typing import List
from collections import defaultdict


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [[-1 for _ in range(d + 1)] for _ in range(n)]

        def dfs(start: int, _d: int):
            if n - start < _d:
                return -1
            if n - start == _d:
                return sum(jobDifficulty[start:])
            if _d == 1:
                return max(jobDifficulty[start:])
            if dp[start][_d] != -1:
                return dp[start][_d]
            min_dif = 1000000
            for i in range(n - _d - start + 1):
                min_dif = min(min_dif, max(jobDifficulty[start: start + i + 1]) + dfs(start + i + 1, _d - 1))
            dp[start][_d] = min_dif
            return min_dif

        return dfs(0, d)


print(Solution().minDifficulty([6, 5, 4, 3, 2, 1], 2))
print(Solution().minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6))
