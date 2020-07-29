def numIslands(grid):
    n_row = len(grid)
    if n_row == 0:
        return 0
    n_col = len(grid[0])
    # f_grid = [i for item in grid for i in item]
    queue = []
    res = 0
    # for i in range(len(f_grid)):
    for i in range(n_row):
        for j in range(n_col):
            # if f_grid[i] == '1':
            if grid[i][j] == '1':
                res += 1
                grid[i][j] = '0'
                # f_grid[i] = '0'
                queue.append((i, j))
                # queue.append(i)
                while queue:
                    row, col = queue.pop(0)
                    # ind = queue.pop(0)
                    # left
                    if col > 0 and grid[row][col - 1] == '1':
                        queue.append((row, col - 1))
                        grid[row][col - 1] = '0'
                    # if ind % n_col != 0 and f_grid[ind - 1] == '1':
                    #     queue.append(ind - 1)
                    #     f_grid[ind - 1] = '0'
                    # right
                    if col + 1 < n_col and grid[row][col + 1] == '1':
                        queue.append((row, col + 1))
                        grid[row][col + 1] = '0'
                    # if (ind + 1) % n_col != 0 and f_grid[ind + 1] == '1':
                    #     queue.append(ind + 1)
                    #     f_grid[ind + 1] = '0'
                    # up
                    if row > 0 and grid[row - 1][col] == '1':
                        queue.append((row - 1, col))
                        grid[row - 1][col] = '0'
                    # if ind > n_col and f_grid[ind - n_col] == '1':
                    #     queue.append(ind - n_col)
                    #     f_grid[ind - n_col] = '0'
                    # down
                    if row + 1 < n_row and grid[row + 1][col] == '1':
                        queue.append((row + 1, col))
                        grid[row + 1][col] = '0'
                    # if ind + n_col < len(f_grid) and f_grid[ind + n_col] == '1':
                    #     queue.append(ind + n_col)
                    #     f_grid[ind + n_col] = '0'
    return res


print(numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
print(numIslands([['1','1']]))
print(numIslands([
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]))
print(numIslands([]))
print(numIslands([['1','1','0','1','0']]))
print(numIslands([['1'],['1'],['0'],['1'],['0']]))
print(numIslands([["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],
                  ["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],
                  ["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],
                  ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                  ["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                  ["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],
                  ["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],
                  ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],
                  ["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
                  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                  ["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
                  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                  ["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
                  ["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],
                  ["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],
                  ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],
                  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
                  ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]))
