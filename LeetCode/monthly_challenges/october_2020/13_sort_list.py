"""
Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge(left, right):
            result = None
            if not left:
                return right
            if not right:
                return left
            if left.val <= right.val:
                result = left
                result.next = merge(left.next, right)
            else:
                result = right
                result.next = merge(left, right.next)
            return result

        def merge_sort(node):
            if not node or not node.next:
                return node
            middle = get_middle_node(node)
            next_to_middle = middle.next
            middle.next = None
            left = merge_sort(node)
            right = merge_sort(next_to_middle)
            sorted_list = merge(left, right)
            return sorted_list


        def get_middle_node(node):
            if not node:
                return None
            slow_ptr = node
            fast_ptr = node
            while fast_ptr.next and fast_ptr.next.next:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            return slow_ptr
        return merge_sort(head)


def print_ll(node):
    if not node:
        return
    print(node.val, end="->")
    print_ll(node.next)

head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

new_ll = Solution().sortList(head)
print_ll(new_ll)

