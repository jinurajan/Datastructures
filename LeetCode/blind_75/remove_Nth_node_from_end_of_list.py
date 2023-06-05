"""
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

edge cases

node to delete can be
- head
- tail
- can LL be empty ?
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        slow = head
        fast = head
        prev = None
        for i in range(n):
            fast = fast.next
        
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        if prev:
            prev.next = slow.next
            return head
        else:
            return head.next
