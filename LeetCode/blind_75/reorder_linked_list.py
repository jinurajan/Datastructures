"""
Reorder List
You are given the head of a singly linked-list. The list can be represented as:

Reorder the list to be on the following form:
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

- number of nodes is in range[1, 5 * pow(10, 4)]
- 1 <= Node.val <= 1000


Thinking
1.find the mid point using slow and fast pointers - O(n)
2.reverse the second half of the linkedlist starting with slow - O(n/2)
3.Run through both the lists and join alternatively until the end - O(n/2)
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, node):
        if not node:
            return node
        prev = None
        current = node

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find the mid point using two pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is the end of the first ll reverse the second half
        l2 = self.reverse(slow.next)
        slow.next = None
        l1 = head
        while l1 and l2:
            new_l2 = l2.next
            new_l1 = l1.next
            l1.next = l2
            l2.next = new_l1
            l1 = new_l1
            l2 = new_l2
        return l1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = deque()
        node = head
        while node:
            stack.append(node)
            node = node.next
        current = head
        while stack:
            next_node = stack.pop()
            if current == next_node or current.next == next_node:
                next_node.next = None
                break
            tmp = current.next
            current.next = next_node
            next_node.next = tmp
            current = tmp

        return head            