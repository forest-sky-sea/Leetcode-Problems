# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_d = self.minDepth(root.left)
        right_d = self.minDepth(root.right)
        if not left_d:
            return right_d + 1
        if not right_d:
            return left_d + 1
        return min(left_d, right_d) + 1


a = TreeNode(3)
a.left = TreeNode(9)
b = TreeNode(20)
b.left = TreeNode(15)
b.right = TreeNode(7)
a.right = b
print(Solution().minDepth(a))
