from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i, a in enumerate(A):
            A[i] = [x ^ 1 for x in a[::-1]]
        return A


s = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(Solution().flipAndInvertImage(s))
