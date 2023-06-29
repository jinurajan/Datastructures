"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


999 + 1 -> 1000

carry, val

length of one is less than another handle that cases

"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode(val=-1)
        node = dummy_head

        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = a+b+carry
            if sum >= 10:
                carry = 1
                val = sum % 10
            else:
                carry = 0
                val = sum
            new_node = ListNode(val=val)
            node.next = new_node
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            node.next = ListNode(val=1)
        
        return dummy_head.next


