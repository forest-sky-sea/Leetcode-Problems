from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top, right, left, bottom = 0, 0, 0, 0
        res = []
        while True:
            # ->
            if n - left - right > 0:
                res.extend(matrix[top][left:n-right])
                top += 1
                if m - bottom - top > 0:
                    # |
                    # v
                    res.extend([matrix[i][n-right-1] for i in range(top, m-bottom)])
                    right += 1
                    if n - left - right > 0:
                        # <-
                        res.extend(matrix[m-bottom-1][left:n-right][::-1])
                        bottom += 1
                        if m - bottom - top > 0:
                            # ^
                            # |
                            res.extend([matrix[i][left] for i in range(top, m-bottom)][::-1])
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


m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(Solution().spiralOrder(m1))
