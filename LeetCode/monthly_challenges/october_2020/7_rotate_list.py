"""
Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        if k == 0:
            return head
        l = self.len(head)
        if k >= l:
            k = k % l
        if k == 0:
            return head
        slow_ptr = head
        fast_ptr = head
        for i in range(k):
            fast_ptr = fast_ptr.next
        while fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        # slow_ptr is at new head position
        new_head = slow_ptr.next
        slow_ptr.next = None
        fast_ptr.next = head
        return new_head

    def len(self, node):
        l = 0
        while node:
            l += 1
            node = node.next
        return l 


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        if k == 0:
            return head
        l, tail = self.get_tail(head)
        k = k % l
        if k == 0:
            return head
        i = k
        fast_ptr = head
        slow_ptr = head
        while i and fast_ptr:
            fast_ptr = fast_ptr.next
            i -= 1
        while fast_ptr:
            new_tail = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        new_tail.next = None
        if tail:
            tail.next = head
        return slow_ptr

    def get_tail(self, node):
        l = 0
        tail = None
        while node:
            tail = node
            l += 1
            node = node.next
        return l, tail


def print_ll(node):
    if not node:
        return
    print(node.val)
    print_ll(node.next)


head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(2)
new_head = Solution().rotateRight(head, 2)
print_ll(new_head)
