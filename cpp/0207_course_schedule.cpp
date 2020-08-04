class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
      vector<int>dst(numCourses);
      vector<vector<int>> arr(numCourses);
      for(int i = 0; i < prerequisites.size(); i++) {
        dst[prerequisites[i][1]]++;
        arr[prerequisites[i][0]].push_back(prerequisites[i][1]) ;
      }

      queue<int> q;

      for(int i = 0; i < numCourses; i ++){
        if (dst[i] == 0) q.push(i);
      }
      int count = 0;

      while(!q.empty()) {
        int cur = q.front();
        // cout << "cur=" << cur << endl;
        q.pop();
        count++;
        for(int i = 0; i < arr[cur].size(); i++) {
          dst[arr[cur][i]]--;
          if (dst[arr[cur][i]] == 0)
            q.push(arr[cur][i]);
        }
      }
      // cout << count<< endl;
      return count == numCourses;
    }
};
