# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def height(node: TreeNode) -> int:
            if not node:
                return 0
            height_l = height(node.left)
            if height_l == -1:
                return -1
            height_r = height(node.right)
            if height_r == -1:
                return -1
            if abs(height_l - height_r) > 1:
                return -1
            return max(height_l, height_r) + 1

        return height(root) != -1


a = TreeNode(3)
b = TreeNode(9)
a.left = b
c = TreeNode(20)
a.right = c
d = TreeNode(15)
c.left = d
e = TreeNode(7)
c.right = e
print(Solution().isBalanced(a))
