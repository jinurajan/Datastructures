"""
Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        def reverse(node):
            prev = None
            current = node
            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            return prev

        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if fast_ptr:
            slow_ptr = slow_ptr.next
        reverse_ll_head = reverse(slow_ptr)
        while head and reverse_ll_head:
            if head.val != reverse_ll_head.val:
                return False
            head = head.next
            reverse_ll_head = reverse_ll_head.next
        return True

