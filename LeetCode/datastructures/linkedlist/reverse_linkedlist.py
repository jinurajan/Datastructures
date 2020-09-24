"""
Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        return self.reverse(None, head, head.next)

    def reverse(self, prev, current, nxt):
        if current.next is None:
            current.next = prev
            return current
        current.next = prev
        return self.reverse(current, nxt, nxt.next)


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = None
        curr = head
        nxt = curr.next
        while curr.next is not None:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = curr.next
        curr.next = prev
        return curr


def print_ll(node):
    while node is not None:
        print node.val,
        node = node.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head = Solution().reverseList(head)
print_ll(head)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head = Solution1().reverseList(head)
print_ll(head)



