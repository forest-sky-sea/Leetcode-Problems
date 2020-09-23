# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover_magic(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1
        num = 0

        def dfs(_root: TreeNode):
            if not _root:
                return 2

            left = dfs(_root.left)
            right = dfs(_root.right)
            if left == 2 and right == 2:
                return 0
            if left == 0 or right == 0:
                nonlocal num
                num += 1
                return 1
            if left == 1 or right == 1:
                return 2

        if dfs(root) == 0:
            num += 1
        return num

    def minCameraCover(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1

        # 要使当前的_root被监控，摄像头可以有3种可选位置：
        # 1. 放在_root处
        # 2. 放在_root的parent处
        # 3. 放在_root的左右其中一个child处
        # 递归函数返回一个三元组，分别记录使当前_root被覆盖，摄像头在三种位置处时所需的最小摄像头数量
        def dfs(_root: TreeNode) -> (int, int, int):
            # 初始化None节点值为(0, 0, 0)
            if not _root:
                return 0, 0, 0

            this_left, parent_left, child_left = dfs(_root.left)
            this_right, parent_right, child_right = dfs(_root.right)
            # 左/右child的摄像头不放在parent处，所需的最小值
            no_parent_left = min(this_left, child_left)
            no_parent_right = min(this_right, child_right)
            # 状态转移函数：
            # 1.摄像头放在_root处，计算以下几种情况的最小值：
            #   1）左child的摄像头放在parent处 + 右child的摄像头放在parent处 - 1
            #   2）左/右child的摄像头放在parent处 + 右/左child的摄像头不放在parent处
            #   3）左和右child的摄像头都不放在parent处 + 1
            if parent_left == 0 and parent_right == 0:
                this_root = 1
            elif parent_right == 0:
                this_root = min(parent_left, no_parent_left + 1)
            elif parent_left == 0:
                this_root = min(parent_right, no_parent_right + 1)
            else:
                this_root = min(parent_left + parent_right - 1,
                                parent_left + no_parent_right,
                                parent_right + no_parent_left,
                                no_parent_left + no_parent_right + 1)
            # 2.放在_root的parent处：
            #   左child的摄像头不放在parent处 + 右child的摄像头不放在parent处 + 1
            #   不用分情况讨论，因为默认值为0
            parent_root = no_parent_left + no_parent_right + 1
            # 3.放在_root的左右其中一个child处，计算以下几种情况的最小值:
            #   1）左右child都有摄像头
            #   2）左/右child有摄像头 + 右/左child的摄像头在各自child处
            if this_left == 0 and this_right == 0:
                child_root = 1
            elif this_left == 0:
                child_root = this_right
            elif this_right == 0:
                child_root = this_left
            else:
                child_root = min(this_left + this_right,
                                 this_left + child_right,
                                 this_right + child_left)
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
# b.right = d
# f.right = g
# e.left = f
# d.left = e
c.left = d
d.right = e
# a.right = b
# b.right = c
# c.right = d

print(Solution().minCameraCover1(a))
