// DFS solution
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
      int y = grid.size();
      if (y == 0)
        return 0;
      int x = grid[0].size();
      

      int res = 0;

      for(int i = 0; i < y ; i++) {
        for (int j = 0; j < x; j++) {
          if (grid[i][j] == '1') {
            ++res;
            dfs(i, j, grid);
          }
        }
      }
      return res;
    }
    void dfs(int r, int c, vector<vector<char>>& grid) {
      grid[r][c] = '0';
    
      if (r - 1 >= 0 && grid[r-1][c] == '1') dfs(r - 1, c, grid);
      if (r + 1 < grid.size() && grid[r+1][c] == '1') dfs(r + 1, c, grid);
      if (c - 1 >= 0 && grid[r][c-1] == '1') dfs(r, c - 1, grid);
      if (c + 1 < grid[0].size() && grid[r][c+1] == '1') dfs(r, c + 1, grid);
    }
};

// BFS solution
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
      int y = grid.size();
      if (y == 0)
        return 0;
      int x = grid[0].size();
    
      int res = 0;
      for (int i = 0; i < y; i++) {
        for (int j = 0; j < x; j++) {
          if(grid[i][j] == '1') {
            ++res;
            grid[i][j] == '0';
            queue<pair<int, int>> next;
            next.push({i, j});
            while(!next.empty()) {
              auto top = next.front();
              next.pop();
              
              if (top.first - 1 >= 0 && grid[top.first-1][top.second] == '1') {
                next.push({top.first-1, top.second});
                grid[top.first-1][top.second] = '0';
              }
              if (top.first + 1 < grid.size() && grid[top.first+1][top.second] == '1') {
                next.push({top.first+1, top.second});
                grid[top.first+1][top.second] = '0';
              }
              if (top.second - 1 >= 0 && grid[top.first][top.second-1] == '1') {
                next.push({top.first, top.second-1});
                grid[top.first][top.second-1] = '0';
              }
              if (top.second + 1 < grid[0].size() && grid[top.first][top.second+1] == '1') {
                next.push({top.first, top.second+1});
                grid[top.first][top.second+1] = '0';
              }
            }
          }
        }
      }

      return res;
    }
    
};

// BFS. use more space but little performance improvement.
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
      int y = grid.size();
      if (y == 0)
        return 0;
      int x = grid[0].size();
    
      int res = 0;
      for (int i = 0; i < y; i++) {
        for (int j = 0; j < x; j++) {
          if(grid[i][j] == '1') {
            ++res;
            grid[i][j] = '0';
            // queue<pair<int, int>> next;
            queue<int> next_i;
            queue<int> next_j;
            // next.push({i, j});
            next_i.push(i);
            next_j.push(j);
            while(!next_i.empty()) {
              // top = next.front();
              // next.pop();
              int r = next_i.front();
              int c = next_j.front();
              next_i.pop();
              next_j.pop();
              
              if (r - 1 >= 0 && grid[r-1][c] == '1') {
                // next.push({top.first-1, top.second});
                next_i.push(r-1);
                next_j.push(c);
                grid[r-1][c] = '0';
              }
              if (r + 1 < grid.size() && grid[r+1][c] == '1') {
                // next.push({top.first+1, top.second});
                next_i.push(r+1);
                next_j.push(c);
                grid[r+1][c] = '0';
              }
              if (c - 1 >= 0 && grid[r][c-1] == '1') {
                // next.push({top.first, top.second-1});
                next_i.push(r);
                next_j.push(c-1);
                grid[r][c-1] = '0';
              }
              if (c + 1 < grid[0].size() && grid[r][c+1] == '1') {
                // next.push({top.first, top.second+1});
                next_i.push(r);
                next_j.push(c+1);
                grid[r][c+1] = '0';
              }
            }
          }
        }
      }

      return res;
    }
    
};
