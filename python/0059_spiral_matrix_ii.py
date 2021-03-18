from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        top, right, left, bottom = 0, n - 1, 0, n - 1
        cur = 1
        while True:
            # cycle
            if left <= right:
                for i in range(left, right + 1):
                    res[top][i] = cur
                    cur += 1
                top += 1
                if top <= bottom:
                    for i in range(top, bottom + 1):
                        res[i][right] = cur
                        cur += 1
                    right -= 1
                    if left <= right:
                        for i in range(right, left - 1, -1):
                            res[bottom][i] = cur
                            cur += 1
                        bottom -= 1
                        if top <= bottom:
                            for i in range(bottom, top - 1, -1):
                                res[i][left] = cur
                                cur += 1
                            left += 1
                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        return res


print(Solution().generateMatrix(3))
