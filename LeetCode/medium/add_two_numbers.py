"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def pad_len(self, head, pad_len):
        node = head
        while node.next is not None:
            node = node.next
        i = 0
        while i < pad_len:
            i += 1
            node.next = ListNode(0)
            node = node.next
        return head

    def length(self, head):
        count = 0
        node = head
        while node is not None:
            count += 1
            node = node.next
        return count

    def addTwoNumbers(self, l1, l2):
        len1 = self.length(l1)
        len2 = self.length(l2)
        if len1 > len2:
            l2 = self.pad_len(l2, len1 - len2)
        else:
            l1 = self.pad_len(l1, len2 - len1)
        result_ll = self.add_list(l1, l2, 0)
        return result_ll

    def add_list(self, ll_1, ll_2, carry):
        if ll_1 is None and ll_1 is None and carry == 0:
            return None
        value = carry
        if ll_1 is not None:
            value += ll_1.val
        if ll_2 is not None:
            value += ll_2.val

        remainder = value % 10
        result = ListNode(remainder)

        if ll_1 is not None or ll_2 is not None:
            more = self.add_list(
                None if ll_1 is None else ll_1.next,
                None if ll_2 is None else ll_2.next,
                1 if value >= 10 else 0)
            result.next = more

        return result


def print_ll(head):
    node = head
    while node is not None:
        print node.val,
        # if node.next is not None:
        #     print "->"
        node = node.next


if __name__ == "__main__":
    l1 = ListNode(0)
    # l1.next = ListNode(9)
    # l1.next.next = ListNode(9)

    l2 = ListNode(7)
    l2.next = ListNode(3)
    # l2.next.next = ListNode(4)
    # print "\n"
    res = Solution().addTwoNumbers(l1, l2)
    print_ll(res)
