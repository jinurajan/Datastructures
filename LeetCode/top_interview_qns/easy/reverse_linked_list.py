"""
Reverse Linked List

Solution
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev = None
        current = head
        next_node = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head = prev
        return head


def printLL(node):
    while node is not None:
        print node.val, "->",
        node = node.next


class SolutionRecursion(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        return self.reverse(current, None, head)

    def reverse(self, current, prev, head):
        if current.next is None:
            head = current
            current.next = prev
            return head
        next_node = current.next
        current.next = prev
        return self.reverse(next_node, current, head)

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    printLL(SolutionRecursion().reverseList(head))
