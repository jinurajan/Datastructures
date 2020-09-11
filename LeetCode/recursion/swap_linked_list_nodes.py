"""
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swap(node):
            if node is None or node.next is None:
                return node
            else:
                new_head = node.next
                node.next = swap(node.next.next)
                new_head.next = node
                return new_head
        if head is None or head.next is None:
            # single element or 0 element:
            return head
        else:
            # multiple elements
            head = swap(head)
            return head


class Solution1(object):
    # This is by exchanging the values.
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        if not head.next:
            return head
        next = head.next.next
        head.val, head.next.val = head.next.val, head.val
        self.swapPairs(next)
        return head


        
            

ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)
head = Solution().swapPairs(ll)

while head is not None:
    print head.val,
    head = head.next

print "\n******"

ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)

head = Solution1().swapPairs(ll)
while head is not None:
    print head.val,
    head = head.next
