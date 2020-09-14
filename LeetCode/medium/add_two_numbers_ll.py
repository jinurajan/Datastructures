"""

2. Add Two Numbers (medium)
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        r = 0
        head = None
        node = None
        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = val1 + val2 + r
            if s >= 10:
                r = 1
                s = s % 10
            else:
                r = 0
            if not head:
                node = ListNode(s)
                head = node
            else:
                node.next = ListNode(s)
                node = node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if r > 0:
            node.next = ListNode(r)

        return head


class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        carry = 0
        head = None
        while  l1 or l2 or carry:
            carry, val = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry, 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not head:
                # its head node:
                head = ListNode(val)
                p = head
            else:
                p.next = ListNode(val)
                p = p.next

        return head




def print_ll(node):
    while node is not None:
        print node.val,
        node = node.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)


l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

head = Solution().addTwoNumbers(l1, l2)
print_ll(head)

head = Solution1().addTwoNumbers(l1, l2)
print_ll(head)

print ""
l1 = ListNode(1)
l1.next = ListNode(8)

l2 = ListNode(0)
head = Solution().addTwoNumbers(l1, l2)
print_ll(head)

head = Solution1().addTwoNumbers(l1, l2)
print_ll(head)



