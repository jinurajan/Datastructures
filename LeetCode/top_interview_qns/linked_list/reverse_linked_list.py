"""
Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        def reverse(prev, curr, nxt):
            if not curr:
                curr.next = prev
                return curr
            curr.next = prev
            return reverse(curr, nxt, nxt.next)

        return reverse(None, head, head.next)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


def print_ll(node):
    if not node:
        return
    print(node.val)
    print_ll(node.next)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head = Solution().reverseList(head)
print_ll(head)