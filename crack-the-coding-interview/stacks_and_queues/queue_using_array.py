"""
Queue Using Array
"""



class Queue(object):
    def __init__(self):
        self.array = []
        self.head = 0
        self.tail = 0
    def add(self, data):
        self.array.append(data)
        self.tail += 1

    def remove(self):
        val = self.array[self.head]
        del self.array[self.head]
        self.tail -= 1
        return val

    def peek(self):
        return self.array[self.head]

    def isEmpty(self):
        return True if not self.array else False


if __name__ == "__main__":
    q = Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    print q.remove()
    print q.peek()
    print q.remove()
    print q.isEmpty()
    print q.remove()
    print q.remove()
    print q.isEmpty()