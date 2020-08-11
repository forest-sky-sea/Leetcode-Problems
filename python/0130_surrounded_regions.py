from typing import List
from collections import deque


class Solution:
    # guided 52ms
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n_row = len(board)
        if n_row <= 2:
            return
        n_col = len(board[0])
        if n_col <= 2:
            return
        queue = deque()
        for i in [0, n_row - 1]:
            for j in range(n_col):
                if board[i][j] == 'O':
                    queue.append((i, j))
        for i in range(1, n_row - 1):
            for j in [0, n_col - 1]:
                if board[i][j] == 'O':
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            board[row][col] = "L"
            # up, down, left, right
            for next_row, next_col in [(row - 1, col), (row, col - 1),
                                       (row + 1, col), (row, col + 1)]:
                if (0 <= next_row < n_row and 0 <= next_col < n_col
                        and board[next_row][next_col] == 'O'):
                    board[next_row][next_col] = 'L'
                    queue.append((next_row, next_col))

        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == 'L':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    # 56ms
    def solve2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n_row = len(board)
        if n_row <= 2:
            return
        n_col = len(board[0])
        if n_col <= 2:
            return
        liberty = [[0 for _ in range(n_col)] for _ in range(n_row)]
        for i in range(n_row):
            for j in range(n_col):
                if i in [0, n_row - 1] or j in [0, n_col - 1]:
                    if board[i][j] == 'O' and liberty[i][j] == 0:
                        liberty[i][j] = 1
                        queue = deque()
                        queue.append((i, j))
                        while queue:
                            row, col = queue.popleft()
                            # up, down, left, right
                            for next_row, next_col in [(row - 1, col), (row, col - 1),
                                                       (row + 1, col), (row, col + 1)]:
                                if (0 <= next_row < n_row and 0 <= next_col < n_col
                                        and board[next_row][next_col] == 'O'
                                        and liberty[next_row][next_col] == 0):
                                    liberty[next_row][next_col] = 1
                                    queue.append((next_row, next_col))

        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == 'O' and liberty[i][j] == 0:
                    board[i][j] = 'X'


b = [['X', 'X', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'X', 'O', 'X'],
     ['X', 'O', 'X', 'X']]
Solution().solve(b)
a = 0
