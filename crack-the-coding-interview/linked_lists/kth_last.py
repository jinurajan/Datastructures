"""
    Return Kth to Last: Implement an algorithm to  nd the kth to last element of a singly linked list.
"""


def KthLastTwoTraversal(head, k):
    """
        1. first traversal to find length: O(N)
        2. second to find the kth last element: O(N)
    """
    length = 0
    current = head
    while current.next is not None:
        length += 1
        current = current.next

    if k > length:
        return None
    index = head
    i = 0
    while i < length - k + 1:
        index = index.next
        i += 1

    return index.data


def KthLastWithTwoPointers(head, k):
    """
        first_ptr moves slowly
        runner will move k initially and
        traverse normally with first_ptr
        later. when runner becomes None first_ptr
        will be the kth last element
    """
    first_ptr = head
    runner = head
    i = 0
    while i < k - 1:
        runner = runner.next
        i += 1
        if runner is None:
            return None

    while runner.next is not None:
        first_ptr = first_ptr.next
        runner = runner.next

    return first_ptr.data


def KthLastUsingRecursion(head, k):
    if head is None:
        return 0
    index = KthLastUsingRecursion(head.next, k) + 1
    if(index == k):
        print head.data
    return index


class LinkedList(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def print_ll(head):

    while head is not None:
        print head.data,
        head = head.next

if __name__ == "__main__":
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
    print_ll(head)
    print "\n"
    print KthLastTwoTraversal(head, 2)
    print KthLastTwoTraversal(head, 3)
    print KthLastTwoTraversal(head, 1)
    print KthLastTwoTraversal(head, 6)

    print KthLastWithTwoPointers(head, 2)
    print KthLastWithTwoPointers(head, 3)
    print KthLastWithTwoPointers(head, 1)
    print KthLastWithTwoPointers(head, 6)

    KthLastUsingRecursion(head, 2)
    KthLastUsingRecursion(head, 3)
    KthLastUsingRecursion(head, 1)
    KthLastUsingRecursion(head, 6)
