"""
Convert Binary Number in a Linked List to Integer
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        node = head
        len = 0
        decimal = 0
        while node is not None:
            len += 1
            node = node.next
        dpoint = len - 1
        node = head
        while node is not None:
            decimal += node.val * pow(2, dpoint)
            dpoint -= 1
            node = node.next
        return decimal


class Solution1(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if head is None:
            return 0
        node = head
        decimal = 0
        while node is None:
            decimal = decimal << 1 | head.val
            head = head.next
        return decimal


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(0)
    head.next.next = ListNode(1)
    print Solution1().getDecimalValue(head)
