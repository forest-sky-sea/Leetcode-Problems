from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        if neighbors is None:
            neighbors = []
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = deque([node])
        res_root = Node(node.val)
        # res_queue = deque([res_root])
        traversed = {node.val: res_root}
        while queue:
            cur = queue.popleft()
            # res_cur = res_queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor.val in traversed.keys():
                    res_neighbor = traversed[neighbor.val]
                else:
                    res_neighbor = Node(neighbor.val)
                    traversed[neighbor.val] = res_neighbor
                    queue.append(neighbor)
                    # res_queue.append(res_neighbor)
                traversed[cur.val].neighbors.append(res_neighbor)
        return res_root


a = Node(0)
b = Node(1)
c = Node(2)
a.neighbors.append(b)
a.neighbors.append(c)
b.neighbors.append(a)
b.neighbors.append(c)
c.neighbors.append(a)
c.neighbors.append(b)

o = Solution().cloneGraph(a)
las = 1
