"""
Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Input: head = []
Output: []
Explanation: The given linked list is empty (null pointer), so return null.


0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random is null or is pointing to some node in the linked list.

"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        dummy_node = Node(x=-1)
        new_list_node = dummy_node
        current_node = head
        
        def copy_node(node):
            if not node:
                return None
            if node in node_map:
                return node_map[node]
            new_node = Node(node.val)
            node_map[node] = new_node
            return new_node
    
        while current_node:
            new_list_node.next = copy_node(current_node)
            if current_node.random:
                new_list_node.next.random = copy_node(current_node.random)
            current_node = current_node.next
            new_list_node = new_list_node.next
        return dummy_node.next

class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        node_map = {}
        node = head
        dummy_node = Node(-1)
        new_node = dummy_node
        while node:
            if node in node_map:
                new_node.next = node_map[node]
            else:
                new_node.next = Node(node.val)
                node_map[node] = new_node.next
            if node.random:
                if node.random in node_map:
                    # already created node
                    new_node.next.random = node_map[node.random]
                else:
                    # new random node not yet visited
                    new_node.next.random = Node(node.random.val)
                    node_map[node.random] = new_node.next.random
            node = node.next
            new_node = new_node.next
        new_head = dummy_node.next
        dummy_node.next = None
        return new_head

class Solution:
    def __init__(self):
        self.visited = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val, None, None)
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return  node



class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        node = head
        while node:
            new_node = Node(node.val, None, None)
            new_node.next = node.next
            node.next = new_node
            node = new_node.next
        node = head
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next

        old_list_node = head
        new_list_node = head.next
        new_head = head.next
        while old_list_node:
            old_list_node.next = old_list_node.next.next
            new_list_node.next = new_list_node.next.next if new_list_node.next else None
            old_list_node = old_list_node.next
            new_list_node = new_list_node.next
        return new_head


def print_l(node):
    if not node:
        print("\n")
        return
    print((node.val, node.random.val if node.random else None),end="->")
    node = node.next
    print_l(node)

head = Node(7)
head.random = None
head.next = Node(13)
head.next.random = head
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head


print_l(head)
new_head = Solution().copyRandomList(head)
print_l(new_head)