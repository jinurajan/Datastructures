"""
Implement dqueue using array and linkedlist
"""



class QueueUsingArray(object):
    def __init__(self):
        self.q = []

    def enqueue(self, val):
        self.q.append(val)

    def dequeue(self):
        return self.q.pop(0) if self.q else None

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class QueueUsingLinkedList(object):
    def __init__(self):
        self.first = None
        self.count = 0
        self.last = None

    def enqueue(self, val):
        if not self.first:
            self.first = ListNode(val)
            self.last = self.first
        else:
            self.last.next = ListNode(val)
            self.last = self.last.next
        self.count += 1

    def dequeue(self):
        if not self.first:
            return None
        val = self.first.val
        self.first = self.first.next
        self.count -= 1
        return val

    def size(self):
        return self.count

    def is_empty(self):
        return self.first == None



q = QueueUsingArray()
print(q.dequeue())
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.size())
print(q.is_empty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())
print(q.is_empty())

print("******")
q = QueueUsingLinkedList()
print(q.dequeue())
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.size())
print(q.is_empty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())
print(q.is_empty())



