from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def check(x: int, y: int) -> bool:
            # north west
            i, j = x - 1, y - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # north
            i, j = x - 1, y
            while i >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
            # north east
            i, j = x - 1, y + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def dfs(row: int):
            # nonlocal n
            if row == n:
                board_s = []
                for i in range(n):
                    board_s.append(''.join(board[i]))
                res.append(board_s)
                return
            for col in range(n):
                if check(row, col):
                    board[row][col] = 'Q'
                    dfs(row + 1)
                    board[row][col] = '.'

        dfs(0)
        return res


a = Solution().solveNQueens(8)
b = 0
