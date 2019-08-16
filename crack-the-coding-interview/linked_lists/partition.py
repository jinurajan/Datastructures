"""
    Partition: Write code to partition a linked list around a value x, such that 
    all nodes less than x come before all nodes greater than or equal to x. 
    If x is contained within the list the values of x only need to be a er the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
    SOLUTION
    EXAMPLE
    Input: 3->5->8->5->10->2->1[partition=5] Output: 3->1->2->10->5->5->8
"""


def partition1(node, x):
    firsthalf = head
    secondhalf = head

    while node is not None:
        next = node.next
        if node.data < x:
            node.next = firsthalf
            firsthalf = node
        else:
            secondhalf.next = node
            secondhalf = node
        node = next
    secondhalf.next = None

    return firsthalf


def partition2(node, x):
    headstart = None
    headend = None
    tailstart = None
    tailend = None
    while node is not None:
        next = node.next
        node.next = None
        if node.data < x:
            if headstart is None:
                headstart = node
                headend = headstart
            else:
                headend.next = node
                headend = node
        else:
            if tailstart is None:
                tailstart = node
                tailend = tailstart
            else:
                tailend.next = node
                tailend = node
        node = next

    if headstart is None:
        # handle if all values are greater than x
        return tailstart

    headend.next = tailstart

    return headstart


class LinkedList(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def print_ll(head):

    while head is not None:
        print head.data,
        head = head.next
        if head is not None:
            print "->",

if __name__ == "__main__":
    head = LinkedList(3)
    head.next = LinkedList(5)
    head.next.next = LinkedList(8)
    head.next.next.next = LinkedList(5)
    head.next.next.next.next = LinkedList(10)
    head.next.next.next.next.next = LinkedList(2)
    head.next.next.next.next.next.next = LinkedList(1)
    print_ll(head)
    print "\n"
    partitioned_ll = partition2(head, 5)
    print_ll(partitioned_ll)
    print "\n"
    partitioned_ll = partition1(head, 5)
    print_ll(partitioned_ll)
