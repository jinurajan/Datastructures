"""
Implement Stack using array

"""




class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isempty(self):
        return True if not self.stack else False


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
