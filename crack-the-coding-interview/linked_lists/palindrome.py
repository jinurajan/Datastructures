"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""


class LinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_ll(node):
    if node is None:
        return None
    if node.next is None:
        head = node
        return head
    node1 = reverse_ll(node.next)
    node1.next = node
    node.next = None
    return node


def is_palindrome(ll):
    node = head
    reversed_ll = reverse_ll(node)
    print_ll()
    print "\n"
    print_ll(reversed_ll)

    while (ll is not None and reversed_ll is not None):
        if ll.data != reversed_ll.data:
            return False
        else:
            ll = ll.next
            reversed_ll = reversed_ll.next

    return True


def print_ll(head):

    while head is not None:
        print head.data,
        head = head.next
        if head is not None:
            print "->",


if __name__ == "__main__":
    head = LinkedListNode(0)
    head.next = LinkedListNode(1)
    head.next.next = LinkedListNode(2)
    head.next.next.next = LinkedListNode(1)
    head.next.next.next.next = LinkedListNode(0)
    print "\n"
    print is_palindrome(head)