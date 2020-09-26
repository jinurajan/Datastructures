"""
Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
 

Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        """
        if not head:
            # empty
            return head

        odd = head
        even = head.next
        evenfirst = even
        even = evenfirst
        while True:
            if not odd or not even or not even.next:
                odd.next = evenfirst
                break
            odd.next = even.next
            odd = even.next

            if not odd.next:
                # list is of odd length
                even.next = None
                odd.next = evenfirst
                break
            even.next = odd.next
            even = odd.next
        return head


class Solution2(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        """
        if not head or not head.next or not head.next.next:
            # empty/single/double
            return head

        odd_head = None
        odd_node = None
        even_head = None
        even_tail = None
        idx = 1
        while head:
            print head.val
            if idx % 2 != 0:
                # odd
                if not odd_head:
                    odd_head = head
                    odd_node = head
                else:
                    odd_node.next = head
                    odd_node = odd_node.next
            else:
                # even
                if not even_head:
                    even_head = head
                    even_tail = head
                else:
                    even_tail.next = head
                    even_tail = even_tail.next
            head = head.next
            idx += 1
        even_tail.next = None
        odd_node.next = even_head
        return odd_head


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        """
        if not head or not head.next or not head.next.next:
            # empty/single/double
            return head
        odd = head
        even = head.next
        evenfirst = even

        def combine(first, second):
            if not first or not first.next:
                # when number of odd nodes are less
                first.next = evenfirst
                return 
            if not second or not second.next:
                # when number of even nodes are less
                first.next = evenfirst
                return
            first.next = first.next.next
            second.next = second.next.next
            combine(first.next, second.next)

        combine(odd, even)
        return head





def print_ll(node):
    if not node:
        print ""
        return
    print node.val, "->",
    print_ll(node.next)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head = Solution2().oddEvenList(head)
print_ll(head)

# head =  None
# head = Solution2().oddEvenList(head)
# print_ll(head)

# head = ListNode(1)
# head = Solution2().oddEvenList(head)
# print_ll(head)

# head = ListNode(1)
# head.next = ListNode(2)
# head = Solution2().oddEvenList(head)
# print_ll(head)

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head = Solution2().oddEvenList(head)
# print_ll(head)





