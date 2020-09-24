"""
Intersection of Two Linked Lists (Easy)

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        l1 = self.length(headA, 0)
        l2 = self.length(headB, 0)
        if l1 > l2:
            diff = l1 -l2
            while diff != 0:
                headA = headA.next
                diff -= 1
        elif l2 > l1:
            diff = l2 - l1
            while  diff != 0:
                headB = headB.next
                diff -= 1

        while headA and headB:
            if headA.next == headB.next:
                return headA.next
            headA = headA.next
            headB = headB.next
        return None         

    def length(self, node, l):
        if node is None:
            return l
        return self.length(node.next, l+1)



class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            A, B = headA, headB
            while A != B:
                print A.val, B.val
                A = A.next if A.next else headB
                B = B.next if B.next else headA
            return A


headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)


headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = headA.next
# headB.next.next.next = headA.next.next

print Solution().getIntersectionNode(headA, headB).val

