"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev = None
        curr = head
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        nxt = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

