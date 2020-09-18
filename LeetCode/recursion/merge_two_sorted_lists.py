"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution3(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        head = None
        node = head
        while l1 is not None and l2 is not None:
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
            # means l1 is bigger than l2 and leftout
            node.next = l1
        if l2:
            node.next = l2

        return head



class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        NOTE: this coding is merging nodes to the smallest starting list
        """
        if not l1:
            return l2
        if not l2:
            return l1
        head = None
        node = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                if not head:
                    head = l1
                    node = head
                else:
                    node.next = l1
                    node = node.next
                l1 = l1.next
            else:
                if not head:
                    head = l2
                    node = head
                else:
                    node.next = l2
                    node = node.next
                l2 = l2.next
        if l1:
            # means l1 is bigger than l2 and leftout
            node.next = l1
        if l2:
            node.next = l2

        return head


class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
    
        NOTE: Uses TAIL RECURSION    
        """

        def merge(node, l1, l2, head):
            if l1 is None and l2 is None:
                return head
            if l1 is None:
                node.next = l2
                return head
            if l2 is None:
                node.next = l1
                return head
            if l1.val <= l2.val:
                if not node:
                    node = l1
                    head = node
                else:
                    node.next = l1
                    node = node.next
                return merge(node, l1.next, l2, head)
            else:
                if not node:
                    node = l2
                    head = node
                else:
                    node.next = l2
                    node = node.next
                return merge(node, l1, l2.next, head)
        if not l1:
            return l2
        if not l2:
            return l1
        head = None
        return merge(head, l1, l2, head)




class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        USES NON TAIL RECURSION
        """
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




def print_ll(node):
    if not node:
        print ""
        return
    print node.val,
    print_ll(node.next)


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

head = Solution().mergeTwoLists(l1, l2)
print_ll(head)

l1 = None
l2 = ListNode(0)
head = Solution().mergeTwoLists(l1, l2)
print_ll(head)


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

head = Solution1().mergeTwoLists(l1, l2)
print_ll(head)


                
