
import sys


class Stack(object):
	def __init__(self):
		self.stack = []

	def push(self, val):
		self.stack.append(val)

	def pop(self):
		return self.stack.pop(0) if self.stack else None

	def is_empty(self):
		return len(self.stack) == 0

	@property
	def size(self):
		return len(self.stack)




def stack_test_client_1():
	stack = Stack()
	for line in sys.stdin:
		s = line.rstrip()
		if s == '-':
			print(stack.pop())
		else:
			stack.push(s)


# stack_test_client()

def stack_test_client():
	stack = Stack()
	i = input()
	if i == '-':
		print(stack.pop())
	else:
		stack.push(i)

stack_test_client_1()