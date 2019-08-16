"""
    Queue Using LinkedList
"""

class LinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def print_ll(head):

    while head is not None:
        print head.data,
        head = head.next
        if head is not None:
            print "->",


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.head is None:
            self.head = LinkedListNode(data)
            self.tail = self.head
        else:
            new_node = LinkedListNode(data)
            self.tail.next = new_node
            self.tail = new_node


    def remove(self):
        if self.head is not None:
            # not empty queue
            val = self.head.data
            self.head = self.head.next
            return val
        else:
            raise Exception('Queue is Empty')

    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            raise Exception('Queue is Empty')

    def isEmpty(self):
        return True if self.head is None else False


if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    print_ll(q.head)
    print "\n"
    print q.remove()
    print q.peek()
    print q.remove()
    print q.isEmpty()
    print q.remove()
    print q.remove()
    print q.isEmpty()