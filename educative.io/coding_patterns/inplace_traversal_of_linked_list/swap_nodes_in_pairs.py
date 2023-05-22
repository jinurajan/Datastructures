"""
Given a singly linked list, swap every two adjacent nodes of the linked list. After the swap, return the head of the linked list.

 Solve the problem without modifying the values in the list’s nodes. In other words, only the nodes themselves can be changed.
"""


def swap_pairs(head):
    if not head or not head.next:
        return head
    next = head.next.next
    head.data, head.next.data = head.next.data, head.data
    swap_pairs(next)
    return head
