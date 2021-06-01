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


class QueueUsing2Stacks(object):
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        if self.stack1.isempty() and self.stack2.isempty():
            raise Exception("Queue is Empty")
        if self.stack2 is None:
            # second stack is empty
            while not self.stack1.isempty():
                x = self.stack1.pop()
                print x
                self.stack2.push(x)
            print self.stack2.stack
        x = self.stack2.peek()
        self.stack2.pop()
        return x


if __name__ == "__main__":
    q = QueueUsing2Stacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print q.stack1.stack
    print q.dequeue()
    # print q.dequeue()
    # print q.dequeue()
    # print q.dequeue()