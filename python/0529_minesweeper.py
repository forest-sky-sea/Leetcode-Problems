from typing import List
from collections import deque


class Solution:
    # do not need check board
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n_row = len(board)
        if n_row == 0:
            return board
        n_col = len(board[0])
        if n_col == 0:
            return board

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        elif board[click[0]][click[1]] == 'E':
            queue = deque([(click[0], click[1])])
            travel = [[False for _ in range(n_col)] for _ in range(n_row)]
            travel[click[0]][click[1]] = True
            while queue:
                i, j = queue.popleft()
                n_mine = 0
                for r_i, r_j in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                                 (i, j - 1), (i, j + 1),
                                 (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                    if 0 <= r_i < n_row and 0 <= r_j < n_col and board[r_i][r_j] == 'M':
                        n_mine += 1
                if n_mine > 0:
                    board[i][j] = str(n_mine)
                else:
                    board[i][j] = 'B'
                    for r_i, r_j in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                                     (i, j - 1), (i, j + 1),
                                     (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                        if (0 <= r_i < n_row and 0 <= r_j < n_col
                                and board[r_i][r_j] == 'E' and not travel[r_i][r_j]):
                            travel[r_i][r_j] = True
                            queue.append((r_i, r_j))

        return board

    def updateBoard2(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n_row = len(board)
        if n_row == 0:
            return board
        n_col = len(board[0])
        if n_col == 0:
            return board
        check_board = [[0 for _ in range(n_col)] for _ in range(n_row)]
        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == 'M':
                    check_board[i][j] = -1
                    for r_i, r_j in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                                     (i, j - 1), (i, j + 1),
                                     (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                        if 0 <= r_i < n_row and 0 <= r_j < n_col:
                            check_board[r_i][r_j] += 1

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        elif board[click[0]][click[1]] == 'E' and check_board[click[0]][click[1]] > 0:
            board[click[0]][click[1]] = str(check_board[click[0]][click[1]])
        elif board[click[0]][click[1]] == 'E' and check_board[click[0]][click[1]] == 0:
            queue = deque([(click[0], click[1])])
            travel = [[0 for _ in range(n_col)] for _ in range(n_row)]
            travel[click[0]][click[1]] = 1
            while queue:
                i, j = queue.popleft()
                board[i][j] = 'B'
                for r_i, r_j in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                                 (i, j - 1), (i, j + 1),
                                 (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                    if 0 <= r_i < n_row and 0 <= r_j < n_col and travel[r_i][r_j] == 0:
                        travel[r_i][r_j] = 1
                        if check_board[r_i][r_j] == 0:
                            queue.append((r_i, r_j))
                        elif check_board[r_i][r_j] > 0:
                            board[r_i][r_j] = str(check_board[r_i][r_j])

        return board


b1 = [['E', 'E', 'E', 'E', 'E'],
      ['E', 'E', 'M', 'E', 'E'],
      ['E', 'E', 'E', 'E', 'E'],
      ['E', 'E', 'E', 'E', 'E']]
b2 = [["E", "E", "E", "E", "E", "E", "E", "E"],
      ["E", "E", "E", "E", "E", "E", "E", "M"],
      ["E", "E", "M", "E", "E", "E", "E", "E"],
      ["M", "E", "E", "E", "E", "E", "E", "E"],
      ["E", "E", "E", "E", "E", "E", "E", "E"],
      ["E", "E", "E", "E", "E", "E", "E", "E"],
      ["E", "E", "E", "E", "E", "E", "E", "E"],
      ["E", "E", "M", "M", "E", "E", "E", "E"]]
c3 = [0, 0]
c1 = [3, 0]
c2 = [0, 2]
print(Solution().updateBoard(b2, [0, 2]))
