# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1

        def dfs(_root: TreeNode):
            # 分别记录（监控当前点，监控parent，监控child）所需的最少监控数，初始化叶子节点值为（1, 1, 1）
            if not _root.left and not _root.right:
                return 1, 1, 1

            this_left, parent_left, child_left = 0, 0, 0
            if _root.left:
                this_left, parent_left, child_left = dfs(_root.left)
            this_right, parent_right, child_right = 0, 0, 0
            if _root.right:
                this_right, parent_right, child_right = dfs(_root.right)

            # 监控parent：1 + 监控左child or 监控左child的child + 监控右child or 监控右child的child
            parent_root = 1 + min(this_left, child_left) + min(this_right, child_right)
            if not _root.right:
                # 监控当前：左child监控parent or 1 + 非左child监控parent
                this_root = min(parent_left, 1 + min(this_left, child_left))
                child_root = this_left
            elif not _root.left:
                this_root = min(parent_right, 1 + min(this_right, child_right))
                child_root = this_right
            else:
                # 监控当前：
                # 左child监控prent + 右child监控parent - 1 or
                # 右child监控prent + 左child监控parent - 1 or
                # 1 + 非左child监控parent + 非右child监控parent
                this_root = min(parent_left + min(this_right, parent_right - 1, child_right),
                                parent_right + min(this_left, parent_left - 1, child_left),
                                1 + min(this_left, child_left) + min(this_right, child_right))
                # 监控child：监控左child + 非右child监控parent or 监控右child + 非左child监控parent
                child_root = min(this_left + min(this_right, child_right),
                                 this_right + min(this_left, child_left))
            return this_root, parent_root, child_root

        put_this, _, put_child = dfs(root)
        return min(put_this, put_child)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
# f = TreeNode(6)
# g = TreeNode(7)
a.left = b
b.left = c
b.right = d
# f.right = g
# e.left = f
# d.left = e
# c.left = d
# d.right = e
# a.right = b
# b.right = c
# c.right = d

print(Solution().minCameraCover(a))
