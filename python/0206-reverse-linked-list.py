# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = new_head
            new_head = cur
            cur = tmp
        return new_head


# lis = ListNode(1, ListNode(2, ListNode(3)))
# lis = None
lis = ListNode(1)
a = Solution().reverseList(lis)
b = 0
