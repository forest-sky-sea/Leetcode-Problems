from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        opened = [False] * len(rooms)
        opened[0] = True

        def dfs(r: int):
            opened[r] = True
            for key in rooms[r]:
                if not opened[key]:
                    dfs(key)

        dfs(0)
        for room in opened:
            if not room:
                return False
        return True

    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False
        opened = [False] * len(rooms)
        opened[0] = True
        queue = deque()
        queue.append(0)
        while queue:
            cur = queue.popleft()
            keys = rooms[cur]
            for key in keys:
                if not opened[key]:
                    queue.append(key)
                    opened[key] = True

        for room in opened:
            if not room:
                return False
        return True


rs = [[1, 3], [3, 0, 1], [2], [0]]
print(Solution().canVisitAllRooms(rs))
