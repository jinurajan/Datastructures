"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        pre_head = res
        quotient = 0

        def sum_one_list(node, q, res):
            while node:
                s = node.val + q
                if s > 9:
                    r = s % 10
                    q = 1
                    s = r
                else:
                    q = 0
                res.next = ListNode(s)
                res = res.next
                node = node.next
            if q:
                res.next = ListNode(q)
        while l1 and l2:
            sum_val = l1.val + l2.val + quotient
            if sum_val > 9:
                remainder = sum_val % 10
                quotient = 1
                sum_val = remainder
            else:
                quotient = 0
            res.next = ListNode(sum_val)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        if not l1 and not l1:
            if quotient:
                res.next = ListNode(quotient)
        if l1:
            sum_one_list(l1, quotient, res)
        if l2:
            sum_one_list(l2, quotient, res)

        return pre_head.next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        head = res
        carry = 0
        import pdb; pdb.set_trace()
        while True:
            s = l1.val + l2.val + carry
            carry = 0
            if s > 9:
                carry = 1
                s %= 10
            res.val = s
            if not l1.next and not l2.next:
                break
            if l1.next:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next:
                l2 = l2.next
            else:
                l2.val = 0
            res.next = ListNode()
            res = res.next
        if carry > 0:
            res.next = ListNode(carry)
        return head




l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

def print_l(node):
    if not node:
        print("\n")
        return
    print(node.val, end="->")
    print_l(node.next)

res = Solution().addTwoNumbers(l1, l2)
print_l(res)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
res = Solution().addTwoNumbers(l1, l2)
print_l(res)

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)

l2 = ListNode(1)
res = Solution().addTwoNumbers(l1, l2)
print_l(res)

l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(1)
res = Solution().addTwoNumbers(l1, l2)
print_l(res)