"""
Implement stack using linkedlist and Array
"""




class StackUsingArray(object):
	def __init__(self):
		self.stack = []

	def push(self, val):
		self.stack.append(val)

	def pop(self):
		return self.stack.pop(-1) if self.stack else None

	def is_empty(self):
		return len(self.stack) == 0

	@property
	def size(self):
		return len(self.stack)
	


class ListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None


class StackUsingLinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	def push(self, val):
		node = ListNode(val)
		node.next = self.head
		self.head = node
		self.size += 1

	def pop(self):
		if not self.head:
			return None
		val = self.head.val
		self.head = self.head.next
		self.size -= 1
		return val

	def is_empty(self):
		return self.head == None

	def size(self):
		return self.size



from collections import deque

class StackUsingdeque(object):

	def __init__(self):
		self.stack = deque()

	def push(self, val):
		self.stack.appendleft(val)

	def pop(self):
		return self.stack.popleft() if self.stack else None

	def is_empty(self):
		return len(self.stack) == 0

	def size(self):
		return len(self.stack)


s1 = StackUsingArray()
print(s1.pop())
print(s1.push(5))
print(s1.push(4))
print(s1.push(3))
print(s1.pop())
print(s1.size)
print(s1.is_empty())
print(s1.pop())
print(s1.pop())
print(s1.is_empty())
print("********")

s2 = StackUsingLinkedList()
print(s2.pop())
print(s2.push(5))
print(s2.push(4))
print(s2.push(3))
print(s2.pop())
print(s2.size)
print(s2.is_empty())
print(s2.pop())
print(s2.pop())
print(s2.is_empty())
print("********")

s3 = StackUsingdeque()
print(s3.pop())
print(s3.push(5))
print(s3.push(4))
print(s3.push(3))
print(s3.pop())
print(s3.size())
print(s3.is_empty())
print(s3.pop())
print(s3.pop())
print(s3.is_empty())







