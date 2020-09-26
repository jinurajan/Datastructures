"""
Remove Linked List Elements


Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            if head.val == val:
                return None
            return head
        else:
            prev = dummy = ListNode()
            curr = dummy.next = head
            while curr:
                if curr.val == val:
                    prev.next = curr.next
                else:
                    prev = curr
                curr = curr.next
            return dummy.next

class Solution2(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next




class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            if head.val == val:
                return None
            return head
        else:
            prev = None
            curr = head
            return self.traverse(head, prev, curr, val)


    def traverse(self, head, prev, curr, val):
        if not curr:
            return head
        if curr.val == val:
            if not prev:
                head = curr.next
            else:
                prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
        return self.traverse(head, prev, curr, val)





def print_ll(node):
    while node is not None:
        print node.val,
        node = node.next
    print "\n"

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

head = Solution().removeElements(head, 6)
print_ll(head)


head = ListNode(1)
head.next = ListNode(2)
head = Solution().removeElements(head, 3)
print_ll(head)

head = Solution().removeElements(head, 2)
print_ll(head)

head = ListNode(1)
head.next = ListNode(2)
head = Solution().removeElements(head, 1)
print_ll(head)

head = ListNode(1)
head.next = ListNode(1)
head = Solution().removeElements(head, 1)
print_ll(head)

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head = Solution().removeElements(head, 1)
print_ll(head)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
head = Solution().removeElements(head, 2)
print_ll(head)




