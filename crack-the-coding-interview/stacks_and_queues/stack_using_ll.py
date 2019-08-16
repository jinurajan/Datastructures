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

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print s.pop()
    print s.peek()
    print s.pop()
    print s.isempty()
    print s.pop()
    print s.pop()
    print s.isempty()
