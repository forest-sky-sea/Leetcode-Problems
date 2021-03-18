from typing import List
from collections import defaultdict


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = defaultdict(list)

        def find_all(in_s: str, in_c: str) -> List[int]:
            if not dp[in_c]:
                find_res = [index for (index, value) in enumerate(in_s) if value == in_c]
                dp[in_c] = find_res
            return dp[in_c]

        res = list(map(lambda x: (x, 1), find_all(s, t[0])))
        if not res:
            return 0
        else:
            for c in t[1:]:
                new_index = find_all(s, c)
                i, j = 0, 0
                count = 0
                new_res = []
                while i < len(new_index) and j < len(res):
                    k, v = res[j]
                    # 略过比key小的index
                    if new_index[i] <= k and count == 0:
                        i += 1
                    elif new_index[i] > k:
                        count += v
                        j += 1
                    else:
                        new_res.append((new_index[i], count))
                        i += 1
                while i < len(new_index):
                    new_res.append((new_index[i], count))
                    i += 1
                res = new_res
        return sum([v for k, v in res])


a = "aacaacca"
b = "ca"
print(Solution().numDistinct(a, b))
