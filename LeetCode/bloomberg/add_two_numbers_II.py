"""
Add Two Numbers II


You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        reverse l1 l2 and sum up and then reverse it
        """

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        new_head = self.sum_of_two(l1, l2)

        return self.reverse(new_head)


    def reverse(self, head):
        if not head:
            return head
        node = head
        prev = None

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev
        
    def sum_of_two(self, l1, l2):
        dummy_head = ListNode()
        node = dummy_head
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            sum_val = a + b + carry

            carry, sum_val = divmod(sum_val, 10)
            node.next = ListNode(sum_val)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            node.next = ListNode(carry)
        
        return dummy_head.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        reverse l1 l2 and sum up and then reverse it
        """
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        total_sum = 0
        carry = 0
        node = ListNode()
        while s1 or s2:
            if s1:
                total_sum += s1.pop()
            if s2:
                total_sum += s2.pop()
            carry, sum_val = divmod(total_sum, 10)
            node.val = sum_val
            head = ListNode(carry)
            head.next = node
            node = head
            total_sum = carry
        
        return node.next if not carry else node

        

        