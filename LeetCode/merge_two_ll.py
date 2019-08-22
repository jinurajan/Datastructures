"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         len1 = self.length(l1)
#         len2 = self.length(l2)
#         if len2 > len1:
#             first_ll = l2
#             second_ll = l1
#         else:
#             first_ll = l1
#             second_ll = l2
#         new_ll_head = None
#         new_ll_tail = None
#         while second_ll is not None:
#             if first_ll.val > second_ll.val:
#                 if new_ll_head is None:
#                     new_node = ListNode(second_ll.val)
#                     new_ll_head = new_node
#                     new_ll_tail = new_ll_head
#                     second_ll = second_ll.next
#                 else:
#                     new_ll_tail.next = ListNode(second_ll.val)
#             else:
#                 if new_ll_head is None:
#                     new_node = ListNode(first_ll.val)
#                     new_ll_head = new_node
#                     new_ll_tail = new_ll_head
#                 else:
#                     new_ll_tail.next = ListNode(first_ll.val)
#                     first_ll = first_ll.next
#             new_ll_tail = new_ll_tail.next
#         new_ll_tail.next = first_ll
#         return new_ll_head

#     def length(self, head):
#         current = head
#         count = 0
#         while current is not None:
#             count += 1
#             current = current.next
#         return count

#     def print_ll(self, head):
#         current = head
#         while current is not None:
#             print current.val,
#             if current.next is not None:
#                 print "->",
#             current = current.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            result = l1
            result.next = self.mergeTwoLists(l1.next, l2)
        else:
            result = l2
            result.next = self.mergeTwoLists(l1, l2.next)

        return result


def print_ll(head):
    current = head
    while current is not None:
        print current.val,
        if current.next is not None:
            print "->",
        current = current.next


if __name__ == "__main__":
    ll_1 = ListNode(1)
    ll_1.next = ListNode(2)
    ll_1.next.next = ListNode(4)
    print_ll(ll_1)
    print "\n"
    ll_2 = ListNode(1)
    ll_2.next = ListNode(3)
    ll_2.next.next = ListNode(4)
    print_ll(ll_2)
    print "\n"
    print_ll(Solution().mergeTwoLists(ll_1, ll_2))
