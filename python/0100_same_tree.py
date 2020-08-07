from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        p_queue = deque()
        q_queue = deque()
        p_queue.append(p)
        q_queue.append(q)
        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()
            # left
            if (p_node.left and not q_node.left) or (not p_node.left and q_node.left):
                return False
            if p_node.left and q_node.left:
                if p_node.left.val != q_node.left.val:
                    return False
                p_queue.append(p_node.left)
                q_queue.append(q_node.left)
            # right
            if (p_node.right and not q_node.right) or (not p_node.right and q_node.right):
                return False
            if p_node.right and q_node.right:
                if p_node.right.val != q_node.right.val:
                    return False
                p_queue.append(p_node.right)
                q_queue.append(q_node.right)

        return True


p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2, TreeNode(3)))
print(Solution().isSameTree(p1, q1))
