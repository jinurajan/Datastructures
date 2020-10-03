"""
Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if head.next.next is None:
            # 2 elements
            return True if head.val == head.next.val else False
        stack = []
        slow_ptr = head
        fast_ptr = head
        while fast_ptr and fast_ptr.next:
            stack.append(slow_ptr)
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if fast_ptr:
            slow_ptr = slow_ptr.next
        while slow_ptr:
            if slow_ptr.val != stack.pop(-1).val:
                return False
            slow_ptr = slow_ptr.next
        return True

def print_ll(node):
    if not node:
        return
    print(node.val)
    print_ll(node.next)

class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if head.next.next is None:
            # 2 elements
            return True if head.val == head.next.val else False

        def reverse(head):
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
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


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(Solution().isPalindrome(head))


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(Solution().isPalindrome(head))

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(0)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(Solution().isPalindrome(head))

head = ListNode(1)
head.next = ListNode(2)
print(Solution().isPalindrome(head))