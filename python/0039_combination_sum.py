from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        s_target = []

        def dfs(_target: int, start: int):
            for ind, cand in enumerate(candidates[start:]):
                if _target > cand:
                    s_target.append(cand)
                    dfs(_target - cand, ind + start)
                    s_target.pop(-1)
                if _target == cand:
                    s_target.append(cand)
                    res.append(s_target.copy())
                    s_target.pop(-1)
                    break
                if _target < cand:
                    break

        dfs(target, 0)
        return res


a = Solution().combinationSum([2, 3, 5], 8)
b = 0
