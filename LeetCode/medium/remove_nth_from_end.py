# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        slow_ptr = head
        fast_ptr = head
        prev_ptr = None
        count = 0
        while count < n:
            count += 1
            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                # len of ll is less than n
                return head 
        while fast_ptr is not None:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        prev_ptr.next = slow_ptr.next
        return head
            


if __name__ == "__main__":
    ll_1 = ListNode(1)
    n = 1
    print

        
        