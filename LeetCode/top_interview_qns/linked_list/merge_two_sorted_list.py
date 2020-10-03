"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        head.next = self.mergeTwoLists(l1, l2)
        return head


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = None
        node = None
        import pdb; pdb.set_trace()
        while l1 and l2:
            if l1.val <= l2.val:
                if not head:
                    head = ListNode(l1.val)
                    node = head
                else:
                    node.next = ListNode(l1.val)
                    node = node.next
                l1 = l1.next
            else:
                if not head:
                    head = ListNode(l2.val)
                    node = head
                else:
                    node.next = ListNode(l2.val)
                    node = node.next
                l2 = l2.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return head



def print_ll(node):
    if not node:
        return
    print(node.val)
    print_ll(node.next)

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next =ListNode(4)

l2 = ListNode(1)
l2.next =ListNode(3)
l2.next.next = ListNode(4)

head = Solution().mergeTwoLists(l1, l2)
print_ll(head)

