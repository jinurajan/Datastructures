"""
Palindrome Linked List

Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        def reverse(node):
            if not node:
                return
            prev = None
            current = node
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if fast_ptr:
            slow_ptr = slow_ptr.next
        
        rev_head = reverse(slow_ptr)
        while head and rev_head:
            if head.val != rev_head.val:
                return False
            head = head.next
            rev_head = rev_head.next
        return True


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front_ptr = head

        def dfs(current_node):
            if current_node:
                if not dfs(current_node.next):
                    return False
                if self.front_ptr.val != current_node.val:
                    return False
                self.front_ptr = self.front_ptr.next
            return True
        
        return dfs(head)