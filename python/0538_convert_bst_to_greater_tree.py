from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = deque()
        cur = root
        cum_sum = 0
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val += cum_sum
                cum_sum = cur.val
                cur = cur.left
        return root


a = TreeNode(5)
a.left = TreeNode(2)
a.right = TreeNode(13)
Solution().convertBST(a)
bb = 0
