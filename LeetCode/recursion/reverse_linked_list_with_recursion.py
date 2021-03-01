"""
Reverse Linked List


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

class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
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
        
        LL = 1->2->3->4->5
        prev = None
        current = 1
        next = 2
        loop 1
            1 -> None
            prev = 1
            current = 2
            next = 3
        loop2
            2 -> 1 -> None
            prev = 2
            current = 3
            next = 4

        loop3 
            3 -> 2 -> 1 -> None
            prev = 3
            current = 4
            next = 5

        loop4
            4 -> 3 -> 2 -> 1 -> None
            prev = 4
            current = 5
            next = None
        
        loop 5
            5 -> 4 -> 3 -> 2 -> 1 -> None
            return current
        """
        if head is None or head.next is None:
            return head
        prev = None
        current = head
        next = head.next
        while current.next is not None:
            current.next = prev
            prev = current
            current = next
            next = current.next
        current.next = prev
        return current



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

def print_ll(node):
    while node is not None:
        print node.val,
        node = node.next

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head = Solution().reverseList(head)
# print_ll(head)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head = Solution1().reverseList(head)
print_ll(head)


        

