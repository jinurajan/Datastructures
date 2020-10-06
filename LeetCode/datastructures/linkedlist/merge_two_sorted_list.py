"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        head = None
        node = None
        while l1 and l2:
            if l1.val <= l2.val:
                if not head:
                    head = ListNode(l1.val)
                    node = head
                else:
                    node.next = ListNode(l1.val)
                    node = node.next
                l1 = l1.next
            else:
                if not head:
                    head = ListNode(l2.val)
                    node = head
                else:
                    node.next = ListNode(l2.val)
                    node = node.next
                l2 = l2.next
    
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return head


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        dummy_node = ListNode()
        node = dummy_node
        def merge(node, l1, l2):
            if not l1 and not l2:
                return
            if not l1:
                node.next = l2
                return
            if not l2:
                node.next = l1
                return
            if l1.val <= l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next
            return merge(node.next, l1, l2)

        merge(node, l1, l2)
        return dummy_node.next


def print_ll(node):
    if not node:
        return
    print(node.val)
    print_ll(node.next)

head1 = ListNode(2)
head2 = ListNode(1)

head = Solution().mergeTwoLists(head1, head2)
print_ll(head)
