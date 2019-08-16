"""
    Remove Dups! Write code to remove duplicates from an unsorted linked list.
    FOLLOW UP
    How would you solve this problem if a temporary bu er is not allowed?
"""


def remove_dups_with_set(head):
    """
        Complexity: O(n)
        Space Complexity: O(n) for set
    """
    global_set = set()

    current = head
    prev = None
    while current.next is not None:
        if current.data in global_set:
            # already visited node.remove this
            prev.next = current.next
        else:
            global_set.add(current.data)
        prev = current
        current = current.next


def remove_dups(head):
    """
        Complexity is O(n2)
    """
    current = head
    runner = head

    while current.next is not None:
        runner = current.next
        while runner.next is not None:
            if current.data == runner.data:
                current.next = runner.next
            runner = runner.next
        current = current.next


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
    head.next.next = LinkedList(2)
    head.next.next.next = LinkedList(3)
    head.next.next.next.next = LinkedList(3)
    remove_dups_with_set(head)
    print_ll(head)
    print "\n"

    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(2)
    head.next.next.next = LinkedList(3)
    head.next.next.next.next = LinkedList(3)
    remove_dups(head)
    print_ll(head)
