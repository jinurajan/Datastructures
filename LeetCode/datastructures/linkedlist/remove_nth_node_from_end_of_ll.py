"""
Remove Nth Node From End of List (Medium)

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
class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        slow_ptr = head
        fast_ptr = head
        for i in range(1, n):
            fast_ptr = fast_ptr.next
        if not fast_ptr:
            # not enough elements in LL
            return head
        prev = None
        while fast_ptr.next is not None:
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        if not prev:
            # head element to be deleted
            head = slow_ptr.next
            return head
        prev.next = slow_ptr.next
        return head
            
  
def print_ll(node):
    if not node:
        print "\n"
        return
    print node.val,
    print_ll(node.next)



class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None

        fast = head
        while  n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            # head to be deleted
            return head.next
        else:
            slow = head
            while fast.next:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
            return head


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

