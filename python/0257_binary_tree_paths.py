# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        res = []
        path = []

        def dfs(node: TreeNode):
            path.append(str(node.val))
            # leaf
            if not node.left and not node.right:
                res.append('->'.join(path))
                return
            if node.left:
                dfs(node.left)
                path.pop(-1)
            if node.right:
                dfs(node.right)
                path.pop(-1)

        dfs(root)
        return res


a = TreeNode(1)
a.left = TreeNode(2)
b = TreeNode(3)
b.right = TreeNode(4)
a.right = b
x = Solution().binaryTreePaths(a)
y = 0
