"""
 Insert into a Sorted Circular Linked List

 Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the original given node.

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        prev, curr = head, head.next
        to_insert = False
        while True:
            if prev.val <= insertVal <= curr.val:
                to_insert = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    to_insert = True
            if to_insert:
                prev.next = Node(insertVal, curr)
                return head
            prev, curr = curr, curr.next
            if prev == head:
                break
        prev.next = Node(insertVal, curr)
        return head


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            a = Node(insertVal)
            a.next = a
            return a

        insertnode = Node(insertVal)

        startnode = head

        node = startnode
        prev = None
        secondlap = False
        while 1:

            # We have prev and current node

            if prev is not None:
                if prev.val <= node.val:
                    if (prev.val <= insertnode.val <= node.val) or secondlap:
                        insert(prev, insertnode, node)
                        break
                else:  # node.val < prev.val
                    if (insertnode.val <= node.val) or (prev.val <= insertnode.val):
                        insert(prev, insertnode, node)
                        break

            prev = node
            node = node.next
            if id(node) == id(startnode): secondlap = True

        return head


def insert(prev, insertnode, crn):
    prev.next = insertnode
    insertnode.next = crn