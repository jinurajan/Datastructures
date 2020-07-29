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
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        t1,t2,prev = head,head,None
        i = 0
        while i < n-1:
            if t1.next == None:
                return None
            t1 = t1.next
            i+=1
        while t1.next != None:
            prev = t2
            t1 = t1.next
            t2 = t2.next
        if t2 == head and prev is None:
            head = t2.next
        else:
            prev.next = t2.next
        return head
        