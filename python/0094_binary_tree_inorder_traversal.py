from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = deque()
        if not root:
            return []

        top = root
        while top or stack:
            if top:
                stack.append(top)
                top = top.left
            else:
                top = stack.pop()
                res.append(top.val)
                top = top.right

        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return []

        def dfs(_root: TreeNode):
            if _root:
                dfs(_root.left)
                res.append(_root.val)
                dfs(_root.right)

        dfs(root)
        return res


a = TreeNode(1)
b = TreeNode(2)
b.left = TreeNode(3)
a.right = b
print(Solution().inorderTraversal(a))
