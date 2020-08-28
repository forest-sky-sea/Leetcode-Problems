from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        route = defaultdict(list)
        for index, ticket in enumerate(tickets):
            route[ticket[0]].append((ticket[1], index))
        for v in route.values():
            v.sort()
        path = ['JFK']
        used = [False] * len(tickets)

        def dfs(inner_path: List[str]):
            if len(inner_path) == len(tickets) + 1:
                return True
            for neighbor, i in route[path[-1]]:
                if not used[i]:
                    used[i] = True
                    inner_path.append(neighbor)
                    if dfs(inner_path):
                        return True
                    used[i] = False
                    inner_path.pop(-1)
            return False

        dfs(path)
        return path


ts = [["JFK", "SFO"],
      ["JFK", "ATL"],
      ["SFO", "ATL"],
      ["ATL", "JFK"],
      ["ATL", "SFO"]]
ts1 = [["JFK", "KUL"],
       ["JFK", "NRT"],
       ["NRT", "JFK"]]
print(Solution().findItinerary(ts))
print(Solution().findItinerary(ts1))
