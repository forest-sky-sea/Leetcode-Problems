from typing import List
from collections import deque


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9
        check_row = [set(range(1, 10)) for _ in range(n)]
        check_col = [set(range(1, 10)) for _ in range(n)]
        check_grid = [set(range(1, 10)) for _ in range(n)]
        check_board = [[set() for _ in range(n)] for _ in range(n)]

        def check(row, col):
            cont = set()
            for k in range(n):
                if not board[row][k] == '.' or not board[k][col] == '.':
                    cont.add(board[-i][k])
            grid_row = row // 3
            grid_col = col // 3
            for _i in range(3):
                for _j in range(3):
                    grid_num = board[_i + grid_row * 3][_j + grid_col * 3]
                    if not grid_num == '.':
                        cont.add(grid_num)
            return set(range(1, 10)) - cont

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    check_value = check(i, j)
                    if len(check_value) == 1


b = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
Solution().solveSudoku(b)
