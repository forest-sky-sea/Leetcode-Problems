from typing import List
from collections import deque, defaultdict


class Solution:
    # 268ms
    # 记录BFS的每条路径，判断遍历点是否在当前路径中
    def canFinish_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dict = defaultdict(list)
        for pre in prerequisites:
            pre_dict[pre[1]].append(pre[0])

        courses_list = list(range(numCourses))
        while courses_list:
            queue = deque()
            queue.append([courses_list[0]])
            traversed = {courses_list[0]}
            while queue:
                link = queue.popleft()
                courses_next = pre_dict[link[-1]]
                for course_next in courses_next:
                    if course_next in link:
                        return False
                    else:
                        queue.append(link + [course_next])
                        traversed.add(course_next)
            courses_list = list(set(courses_list) - traversed)
        return True

    # 64ms
    # guided 使用拓扑法，无环 = 总有点入度为0
    def canFinish_bfs2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dict = defaultdict(list)
        # 计算每个点入度 (直接依赖点个数)
        degree_dict = [0] * numCourses
        for pre in prerequisites:
            pre_dict[pre[1]].append(pre[0])
            degree_dict[pre[0]] += 1

        # 入度为0 = 谁都不依赖
        queue = deque([i for i in range(numCourses) if degree_dict[i] == 0])
        while queue:
            course = queue.popleft()
            # 删除该点，并其依赖的点度数减一
            numCourses -= 1
            for course_next in pre_dict[course]:
                degree_dict[course_next] -= 1
                if degree_dict[course_next] == 0:
                    queue.append(course_next)
        return numCourses == 0

    # 60ms
    # dfs每条路径，注意两种区别：1. 出现在当前路径中；2. 已经搜索过 (出现在其他路径中)
    def canFinish_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dict = defaultdict(list)
        for pre in prerequisites:
            pre_dict[pre[1]].append(pre[0])

        def dfs(root):
            if traversed[root] == 1:
                return False
            if traversed[root] == 2:
                return True
            # 当前路径记录
            traversed[root] = 1
            for child in pre_dict[root]:
                if not dfs(child):
                    return False
            # 回溯，表示已经搜到过
            traversed[root] = 2
            return True

        traversed = [0] * numCourses
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

    # 724ms
    # 对依赖边进行dfs
    def canFinish_dfs2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 搜索同时删除每次使用的边
        def find_next(course: int) -> List[int]:
            next_c = []
            for r in prerequisites:
                if r[0] == course:
                    next_c.append(r[1])
                    prerequisites.remove(r)
            return next_c

        def dfs(root, path):
            if root in path:
                return False
            new_path = path.copy()
            new_path.add(root)
            for child in find_next(root):
                if not dfs(child, new_path):
                    return False
            return True

        res = True
        while prerequisites and res:
            res = dfs(prerequisites[0][0], set())
        return res

    # 2424ms
    # brute force 遍历所有依赖，并建立依赖表。如果表中有对角元素则出现循环依赖
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep_table = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        if not prerequisites:
            return True
        for pre in prerequisites:
            for i in range(numCourses):
                if dep_table[pre[1]][i] == 1:
                    dep_table[pre[0]][i] = 1
                    if dep_table[i][pre[0]] == 1:
                        return False
            dep_table[pre[0]][pre[1]] = 1
            if dep_table[pre[1]][pre[0]] == 1:
                return False
        return True


print(Solution().canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]))
print(Solution().canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]))
print(Solution().canFinish(3, [[1,0],[2,0]]))
print(Solution().canFinish(2, [[1,0]]))
print(Solution().canFinish(3, [[0,2],[1,2],[2,0]]))
print(Solution().canFinish(4, [[0,1],[2,3],[1,2],[3,0]]))
print(Solution().canFinish(1, []))
print(Solution().canFinish(3, [[1,0],[1,2],[0,1]]))
print(Solution().canFinish(2, [[1,0],[0,1]]))
