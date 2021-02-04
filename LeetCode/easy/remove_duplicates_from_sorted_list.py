"""
Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Input: head = [1,1,1,2,3]
Output: [2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast:
            if fast.next is None and slow.val == fast.val:
                slow.next = None
                return head
            if slow.val == fast.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        return head

def print_l(node):
    if not node:
        print("\n")
        return
    print(node.val, end= "->")
    print_l(node.next)

l = ListNode(1)
l.next =ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)
l.next.next.next.next.next = ListNode(4)
l.next.next.next.next.next.next = ListNode(5)

print_l(l)
new_l = Solution().deleteDuplicates(l)
print_l(new_l)


l = ListNode(1)
l.next =ListNode(1)
l.next.next = ListNode(1)
print_l(l)
new_l = Solution().deleteDuplicates(l)
print_l(new_l)


