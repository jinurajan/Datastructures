"""
Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→

You may not modify the values in the list's nodes, only nodes itself may be changed.

Given 1->2->3->4, reorder it to 1->4->2->3.

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        Q = deque()
        node = head
        while node:
            Q.append(node)
            node = node.next

        node = head
        while Q:
            next_node = Q.pop()
            if node == next_node or node.next == next_node:
                # odd number linkedlist
                next_node.next = None
                break
            new_node = node.next
            node.next = next_node
            next_node.next = new_node
            node = new_node
        return head

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

def print_l(node):
    if not node:
        print("\n")
        return
    print(node.val, end="->")
    print_l(node.next)

print_l(l)

new_l = Solution().reorderList(l)
print_l(new_l)

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
new_l = Solution().reorderList(l)
print_l(new_l)

