from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_ind = inorder.index(root_val)
        left = inorder[:root_ind]
        right = inorder[root_ind + 1:]
        root.left = self.buildTree(left, postorder[:len(left)])
        root.right = self.buildTree(right, postorder[len(left): -1])
        return root


a = [9, 3, 15, 20, 7]
b = [9, 15, 7, 20, 3]
c = Solution().buildTree(a, b)
d = 0
