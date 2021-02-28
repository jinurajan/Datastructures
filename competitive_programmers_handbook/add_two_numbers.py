"""
Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy_node = ListNode()
        node = dummy_node
        rem = 0
        while l1 or l2:
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val
            s = l1_val + l2_val + rem
            if s >= 10:
                rem = 1
                s = s % 10
            else:
                rem = 0
            node.next = ListNode(s)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if rem:
            node.next = ListNode(rem)
            node = node.next
        return dummy_node.next
