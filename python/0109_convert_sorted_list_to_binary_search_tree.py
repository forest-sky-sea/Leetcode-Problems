# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 二分搜索树中序遍历 == 按序输出
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        def build_tree(s: int, t: int):
            if s > t:
                return None
            k = (s + t) // 2
            root = TreeNode()
            root.left = build_tree(s, k - 1)
            # 输出序号k == 按序为序号k赋值
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = build_tree(k + 1, t)
            return root

        len_l = 0
        count_head = head
        while count_head:
            len_l += 1
            count_head = count_head.next
        return build_tree(0, len_l - 1)

    def sortedListToBST2(self, head: ListNode) -> TreeNode:
        def mid_tree(s: ListNode, t: ListNode) -> ListNode:
            fast, slow = s, s
            while fast != t and fast.next != t:
                fast = fast.next.next
                slow = slow.next
            return slow

        def build_tree(node_s: ListNode, node_t: ListNode):
            if node_s == node_t:
                return None
            k = mid_tree(node_s, node_t)
            root = TreeNode(k.val)
            root.left = build_tree(node_s, k)
            root.right = build_tree(k.next, node_t)
            return root

        return build_tree(head, None)

    def sortedListToBST1(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        head_l = []
        while head:
            head_l.append(head.val)
            head = head.next

        def build_tree(tree_l: List):
            k = len(tree_l)
            if k == 1:
                return TreeNode(tree_l[0])
            if k == 2:
                return TreeNode(tree_l[1], left=TreeNode(tree_l[0]))
            half = k // 2
            root = TreeNode(tree_l[half])
            root.left = build_tree(tree_l[0: half])
            root.right = build_tree(tree_l[half + 1: k])
            return root

        return build_tree(head_l)


a = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
b = Solution().sortedListToBST(a)
c = 0
