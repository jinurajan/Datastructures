"""
Flatten a Multilevel Doubly Linked List

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

"""

"""
# Definition for a Node.

"""

from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        
        def dfs(node):
            if not node:
                return
            next_node = node.next
            tail_node = node
            if node.child:
                tail_node = dfs(node.child)
                node.next = node.child
                node.child.prev = node
                tail_node.next = next_node
                if next_node:
                    next_node.prev = tail_node
            ret = dfs(next_node)
            node.child = None
            return ret if ret else tail_node
        
        dfs(head)
        return head
        