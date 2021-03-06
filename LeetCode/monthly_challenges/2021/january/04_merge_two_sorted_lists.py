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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        def merge(new_node, l1, l2):
            if not l1 and not l2:
                return None
            if not l1:
                new_node.next = l2
                return
            elif not l2:
                new_node.next = l1
                return
            if l1.val < l2.val:
                new_node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                new_node.next = ListNode(l2.val)
                l2 = l2.next
            return merge(new_node.next, l1, l2)

        dummy_node = ListNode()
        merge(dummy_node, l1, l2)
        return dummy_node.next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return  l1


l1 = ListNode(1)
l1.next =ListNode(2)
l1.next.next = ListNode(4)


l2= ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

def print_ll(l):
    if not l:
        print("\n")
        return
    print(l.val, end="->")
    print_ll(l.next)

# print_ll(l1)
# print_ll(l2)

new_l = Solution().mergeTwoLists(l1, l2)
print_ll(new_l)

print_ll(Solution().mergeTwoLists(None, None))

print_ll(Solution().mergeTwoLists(None, ListNode(0)))


