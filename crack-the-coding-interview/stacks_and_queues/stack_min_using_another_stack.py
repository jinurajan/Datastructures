"""
    Stack using linkedlist
"""



class LinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            # empty stack
            self.head = LinkedListNode(data)
        else:
            new_node = LinkedListNode(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is not None:
            val = self.head.data
            self.head = self.head.next
            return val
        else:
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


class StackMin(object):
    def __init__(self):
        self.head = None
        self.min_stack = Stack()

    def push(self, data):
        if self.head is None:
            # empty stack
            self.head = LinkedListNode(data)
            if self.min_stack.isempty():
                # empty min_stack
                self.min_stack.push(data)
        else:
            new_node = LinkedListNode(data)
            new_node.next = self.head
            self.head = new_node
            if self.min_stack.peek() > data:
                self.min_stack.push(data)

    def pop(self):
        if self.head is not None:
            val = self.head.data
            self.head = self.head.next
            if self.min_stack.peek() >= val:
                self.min_stack.pop()
            return val
        else:
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
        if self.min_stack.isempty():
            return None
        else:
            return self.min_stack.peek()

if __name__ == "__main__":
    s = StackMin()
    s.push(4)
    print "min is", s.minimum()
    s.push(2)
    print "min is", s.minimum()
    s.push(3)
    print "min is", s.minimum()
    s.push(1)
    print "min is", s.minimum()
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
