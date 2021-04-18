"""
Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow_ptr = head
        fast_ptr = head
        for i in range(n):
            fast_ptr = fast_ptr.next
        if not fast_ptr:
            # first element to be return
            return head.next
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        slow_ptr.next = slow_ptr.next.next
        return head

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast_ptr = head
        for i in range(1, n):
            fast_ptr = fast_ptr.next

        prev = None
        curr = head
        nxt = curr.next
        while fast_ptr.next:
            fast_ptr = fast_ptr.next
            prev = curr
            curr = nxt
            nxt = curr.next
        if not prev:
            # first element to be removed
            return curr.next
        prev.next = nxt
        return head


def print_ll(node):
    if not node:
        print()
        return
    print(node.val, end="->")
    print_ll(node.next)

def make_ll(array):
    head = None
    node = None
    for n in array:
        new_node = ListNode(n)
        if not node:
            head = new_node
            node = new_node
        else:
            node.next = new_node
            node = node.next
    return head



LL = make_ll([1])
print_ll(Solution().removeNthFromEnd(LL, 1))

LL = make_ll([1, 2])
print_ll(Solution().removeNthFromEnd(LL, 1))
#
LL = make_ll([1, 2])
print_ll(Solution().removeNthFromEnd(LL, 2))

LL = make_ll([1,2,3,4,5])
print_ll(Solution().removeNthFromEnd(LL, 2))

LL = make_ll([1,2,3,4,5])
print_ll(Solution().removeNthFromEnd(LL, 1))
LL = make_ll([1,2,3,4,5])
print_ll(Solution().removeNthFromEnd(LL, 2))
LL = make_ll([1,2,3,4,5])
print_ll(Solution().removeNthFromEnd(LL, 3))
LL = make_ll([1,2,3,4,5])
print_ll(Solution().removeNthFromEnd(LL, 4))
LL = make_ll([1,2,3,4,5])
print_ll(Solution().removeNthFromEnd(LL, 5))

