# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0, 0
            if not node.left and not node.right:
                return node.val, 0
            use_left, no_use_left, use_right, no_use_right = 0, 0, 0, 0
            if node.left:
                use_left, no_use_left = dfs(node.left)
            if node.right:
                use_right, no_use_right = dfs(node.right)
            use = node.val + no_use_left + no_use_right
            no_use = max(no_use_left + no_use_right, no_use_left + use_right,
                         use_left + no_use_right, use_left + use_right)
            return use, no_use

        return max(dfs(root))


a = TreeNode(3)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.right = TreeNode(3)
a.right.right = TreeNode(1)
print(Solution().rob(a))
