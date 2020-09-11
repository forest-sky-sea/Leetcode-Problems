from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        sum_ind = []
        for i in range(1, 10):
            sum_ind.append([sum(range(i, j)) for j in range(i, 11)])
        res = []
        res_c = []

        def dfs(_n: int, start: int):
            for i in range(start, 9 - (k - len(res_c) - 2)):
                remain = k - len(res_c)
                if remain == 1:
                    if i <= _n <= 9:
                        res.append(res_c + [_n])
                    break
                min_remain = sum_ind[i - 1][remain]
                if _n == min_remain:
                    res.append(res_c + list(range(i, i + remain)))
                    break
                if _n > min_remain:
                    res_c.append(i)
                    dfs(_n - i, i + 1)
                    res_c.pop(-1)
                else:
                    break

        dfs(n, 1)
        return res


c = Solution().combinationSum3(3, 9)
a = Solution().combinationSum3(3, 7)
b = 0
