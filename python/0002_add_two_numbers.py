class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode):
    # s = 0
    # c = 0
    # s += l1.val
    # s += l2.val
    # if s >= 10:
    #     s -= 10
    #     c = 1
    # head = ListNode(s)
    # cur = head
    # l1 = l1.next
    # l2 = l2.next
    # dummy head
    head = cur = ListNode(0)
    c = 0
    while l1 or l2:
        s = 0
        if l1:
            s += l1.val
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next
        s += c
        if s >= 10:
            c = 1
            s -= 10
        else:
            c = 0
        cur.next = ListNode(s)
        cur = cur.next
    if c == 1:
        cur.next = ListNode(1)
    return head.next


la = ListNode(2)
la.next = ListNode(4)
la.next.next = ListNode(3)

lb = ListNode(5)
lb.next = ListNode(6)
# lb.next.next = ListNode(4)

l3 = add_two_numbers(la, lb)
