"""
    Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the  rst and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
    SOLUTION
    EXAMPLE
    input:the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a->b->d->e->f
"""


def delete_middle_node(node):
    if node is None or node.next is None:
        return node

    node.data = node.next.data
    node.next = node.next.next


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
    head.next.next.next.next.next = LinkedList(6)
    print_ll(head)
    print "\n"
    delete_middle_node(head.next.next.next)
    print_ll(head)
