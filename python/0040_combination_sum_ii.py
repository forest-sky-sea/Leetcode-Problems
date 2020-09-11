from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        res_c = []

        def dfs(_target: int, start: int):
            last = -1
            for ind, cand in enumerate(candidates[start:]):
                if cand == last:
                    continue
                if _target > cand:
                    res_c.append(cand)
                    dfs(_target - cand, start + ind + 1)
                    res_c.pop(-1)
                    last = cand
                elif _target == cand:
                    res.append(res_c + [cand])
                    break
                else:
                    break

        dfs(target, 0)
        return res


a = Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
b = 9
