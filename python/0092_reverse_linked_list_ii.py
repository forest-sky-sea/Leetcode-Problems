# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy_head = ListNode()
        dummy_head.next = head
        cur = dummy_head
        for _ in range(1, left):
            cur = cur.next
        new_head = cur
        cur = cur.next
        rev_tail = ListNode(cur.val)
        rev_head = rev_tail
        cur = cur.next
        for _ in range(left + 1, right + 1):
            tmp = ListNode(cur.val, rev_head)
            rev_head = tmp
            cur = cur.next
        rev_tail.next = cur
        new_head.next = rev_head
        return dummy_head.next


li = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().reverseBetween(li, 2, 4)
