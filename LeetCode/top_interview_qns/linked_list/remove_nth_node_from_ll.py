"""
Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        1. could be head
        2. could be tail
        3. could be in between
        """
        if not head.next: return None
        slow_ptr, fast_ptr = head, head
        k = 1
        while k < n:
            fast_ptr = fast_ptr.next
            k += 1
        if not fast_ptr.next:
            head = head.next
            return head
        prev = None
        while fast_ptr.next:
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        prev.next = slow_ptr.next
        return head


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

head = Solution().removeNthFromEnd(head, 2)
print_ll(head)

head = ListNode(1)
head = Solution().removeNthFromEnd(head, 1)
print_ll(head)

head = ListNode(1)
head.next = ListNode(2)
head = Solution().removeNthFromEnd(head, 2)
print_ll(head)



