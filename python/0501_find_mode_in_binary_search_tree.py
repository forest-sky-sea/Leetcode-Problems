from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        modes = []
        num, mode_num = 0, 0

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            nonlocal num, mode_num, modes
            if not modes:
                modes.append(node.val)
                num += 1
            elif node.val == modes[-1]:
                num += 1
            else:
                if num > mode_num:
                    modes = [modes[-1]]
                    mode_num = num
                elif num < mode_num:
                    modes.pop(-1)
                modes.append(node.val)
                num = 1
            dfs(node.right)

        dfs(root)
        if num > mode_num:
            modes = [modes[-1]]
        elif num < mode_num:
            modes.pop(-1)
        return modes


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(4)
e = TreeNode(5)
a.right = b
b.left = c
# c.left = d
# d.right = e
print(Solution().findMode(a))
