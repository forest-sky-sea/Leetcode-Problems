from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        last = -99999
        min_diff = 99999
        stack = deque()
        cur = root
        while stack or root:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                diff = cur.val - last
                if diff == 0:
                    return 0
                if diff < min_diff:
                    min_diff = diff
                last = cur.val
                cur = cur.right
        return min_diff
