"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()

def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow:
      break
  return cycle_length

def find_start(k, head):
  slow = head
  fast = head
  while k > 0:
    fast = fast.next
    k -= 1
  while slow != fast:
    slow = slow.next
    fast = fast.next
  return slow



def find_cycle_start(head):
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      cycle_length = calculate_cycle_length(slow)
      break
  return find_start(cycle_length, head)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head
print("LinkedList cycle start: " + str(find_cycle_start(head).value))


