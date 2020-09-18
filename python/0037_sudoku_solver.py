from collections import deque
from typing import List, Set


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def row_col_2_grid(row: int, col: int) -> int:
            return row // 3 * 3 + col // 3

        def get_others_in_grid(row: int, col: int):
            x = [0, 1, 2]
            x.remove(row // 3)
            y = [0, 1, 2]
            y.remove(col // 3)
            ret = []
            for _i in x:
                for _j in y:
                    ret.append((_i + row // 3 * 3, _j + col // 3 * 3))
            return ret

        row_board = [[] for _ in range(9)]
        col_board = [[] for _ in range(9)]
        grid_board = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if not board[i][j] == '.':
                    _num = int(board[i][j])
                    row_board[i].append(_num)
                    col_board[j].append(_num)
                    grid_board[row_col_2_grid(i, j)].append(_num)

        check_board = [[set() for _ in range(9)] for _ in range(9)]

        def check(row, col) -> Set[int]:
            cont = set()
            cont |= set(row_board[row])
            cont |= set(col_board[col])
            cont |= set(grid_board[row_col_2_grid(row, col)])
            return set(range(1, 10)) - cont

        def update(add_flag, _queue):
            ret_queue = deque()

            def _update(row, col, num):
                def _update_and_append_queue(_row, _col):
                    if add_flag:
                        if num in check_board[_row][_col]:
                            check_board[_row][_col].remove(num)
                            if len(check_board[_row][_col]) == 1:
                                _queue.append((_row, _col))
                    else:
                        check_board[_row][_col].add(num)

                for _i in range(9):
                    if board[row][_i] == '.':
                        _update_and_append_queue(row, _i)
                    if board[_i][col] == '.':
                        _update_and_append_queue(_i, col)

                for cb_i, cb_j in get_others_in_grid(row, col):
                    if board[cb_i][cb_j] == '.':
                        _update_and_append_queue(cb_i, cb_j)

            while _queue:
                _row, _col = _queue.popleft()
                ret_queue.append((_row, _col))
                board[_row][_col] = str(check_board[_row][_col].pop())
                _update(_row, _col, int(board[_row][_col]))
            return ret_queue

        queue = deque()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    check_value = check(i, j)
                    check_board[i][j] = check_value
                    if len(check_value) == 1:
                        queue.append((i, j))

        # first round
        update(True, queue)

        def next_sudoku(ind):
            for _ind in range(ind, 9 * 9):
                if board[ind // 9][ind % 9] == '.':
                    return _ind
            return -1

        # dfs
        def dfs(ind):
            row, col = ind // 9, ind % 9
            if not check_board[row][col]:
                return False
            for ava in check_board[row][col]:
                board[row][col] = str(check_board[row][col].pop())
                roll_back = update(True, deque((row, col)))
                next_ind = next_sudoku(ind)
                if next_ind == -1:
                    return True
                if dfs(next_ind):
                    return True
                board[row][col] = '.'
                update(False, roll_back)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    dfs(i * 9 + j)
                    break


b = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
b2 = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
      ["7", ".", ".", ".", ".", ".", ".", ".", "."],
      [".", "2", ".", "1", ".", "9", ".", ".", "."],
      [".", ".", "7", ".", ".", ".", "2", "4", "."],
      [".", "6", "4", ".", "1", ".", "5", "9", "."],
      [".", "9", "8", ".", ".", ".", "3", ".", "."],
      [".", ".", ".", "8", ".", "3", ".", "2", "."],
      [".", ".", ".", ".", ".", ".", ".", ".", "6"],
      [".", ".", ".", "2", "7", "5", "9", ".", "."]]
Solution().solveSudoku(b2)
