"""
Reorder List
Given a singly linked list L: L0 -> L1 -> ... -> Ln-1 ->Ln,
reorder it to: L0-> Ln-> L1-> Ln-1-> L2-> Ln-2-> ...

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        slow_ptr = head
        fast_ptr = slow_ptr.next

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        head1 = head
        head2 = self.reverseList(slow_ptr.next)
        head = ListNode(val=0)
        slow_ptr.next = None
        current = head
        while head1 is not None or head2 is not None:
            if head1:
                current.next = head1
                current = current.next
                head1 = head1.next
            if head2:
                current.next = head2
                current = current.next
                head2 = head2.next
        head = head.next
        return head

    def reverseList(self, head):
        prev = None
        current = head
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head

    def printLL(self, head):
        temp = head
        while temp is not None:
            print temp.val, '->',
            temp = temp.next
        print ""


LL = ListNode(val=1)
LL.next = ListNode(val=2)
LL.next.next = ListNode(val=3)
LL.next.next.next = ListNode(val=4)
head = Solution().reorderList(LL)
Solution().printLL(head)
LL.next.next.next.next = ListNode(val=5)
head = Solution().reorderList(LL)
Solution().printLL(head)
