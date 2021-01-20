"""
 Merge Two Sorted Lists
 Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []

Input: l1 = [], l2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:


        def merge(new_node, l1, l2):
            if not l1:
                return None
            elif not l2:
                return None
            if l1.val < l2.val:
                new_node.next = merge(new_node, l1.next, l2)
            else:
                new_node.next = merge(new_node, l1, l2.next)

