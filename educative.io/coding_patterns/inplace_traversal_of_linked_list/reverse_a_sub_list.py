"""
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
"""
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
  # TODO: Write your code here
  if p == q:
    return head
  # find p-1 th node and q+1th node. reverse the nodes in between and link those
  i = 1
  curr, prev = head, None
  while curr and i < p:
    prev = curr
    curr = curr.next
    i += 1
  last_node_of_first = prev

  last_node_after_reversing = curr

  i = 0
  while curr and i < q-p+1:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
    i+= 1

  if last_node_of_first:
    last_node_of_first.next = prev
  else:
    head = prev

  last_node_after_reversing.next = curr
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
