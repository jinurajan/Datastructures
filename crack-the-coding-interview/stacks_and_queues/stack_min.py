"""
    Stack using linkedlist with minimum
"""


class LinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.min_val = None
        self.next = None


class Stack(object):
    def __init__(self):
        self.head = None
        self.min = None

    def push(self, data):
        if self.head is None:
            # empty stack
            self.head = LinkedListNode(data)
            self.head.min_val = data
            self.min = data
        else:
            new_node = LinkedListNode(data)
            new_node.next = self.head
            new_node.min_val = self.min
            self.head = new_node
        if self.min > data:
            self.min = data

    def pop(self):
        if self.head is not None:
            val = self.head.data
            self.min = self.head.min_val
            self.head = self.head.next
            return val
        else:
            self.min = None
            raise Exception('Stack is Empty')

    def peek(self):
        if self.head is not None:
            return self.head.data
        else:
            raise Exception('Stack is Empty')

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def minimum(self):
        if self.head is None:
            return None
        elif self.min is None:
            raise Exception('Stack is Empty')
        else:
            return self.min

if __name__ == "__main__":
    s = Stack()
    s.push(4)
    print "min is", s.minimum()
    s.push(2)
    print "min is", s.minimum()
    s.push(3)
    print "min is", s.minimum()
    s.push(1)
    print "min is", s.minimum()
    print "\n"
    print s.pop()
    print "min is", s.minimum()
    print s.peek()
    print s.pop()
    print "min is", s.minimum()
    print s.isempty()
    print s.pop()
    print "min is", s.minimum()
    print s.pop()
    print "min is", s.minimum()
    print s.isempty()
