# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        ret_tree = TreeNode(t1.val + t2.val)
        ret_tree.left = self.mergeTrees(t1.left, t2.left)
        ret_tree.right = self.mergeTrees(t1.right, t2.right)

        return ret_tree


a = TreeNode(1)
b = TreeNode(2)
b.left = TreeNode(3)
b.right = TreeNode(4)
a.left = b
c = TreeNode(1)
d = TreeNode(5)
d.left = TreeNode(6)
c.left = d
Solution().mergeTrees(a, c)

