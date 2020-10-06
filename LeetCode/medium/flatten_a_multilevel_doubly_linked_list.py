"""
Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 

Constraints:

Number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5 
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

    	def helper(node):
    		if not node:
    			return
    		# save next node for next iteration
    		next_node = node.next
    		tail_node = node
    		if node.child:
    			tail_node = helper(node.child)
    			# link current nodes next to child and its prev to node
    			node.next = node.child
    			node.child.prev = node
    			# find the tail node of child and point its next to next_node which we saved
    			tail_node.next = next_node
    			if next_node:
    				# if next node exists set the tail node as prev
    				next_node.prev = tail_node
    		# once we return we remove child reference. loop will reach every time
    		# once after child operation is done in every recursion
    		ret = helper(next_node)
    		node.child = None
    		return ret if ret else tail_node
    	import pdb; pdb.set_trace()
    	helper(head)
    	return head



def print_ll(node):
	if not node:
		return
	print(node.val)
	print_ll(node.next)







head = Node(1)
head.next = Node(2, head)
head1 = Node(7, head.next.next)
head2 = Node(11, head1.next)
head2.next = Node(12, head2)
head1.next = Node(8, head1, child=head2)
head1.next.next = Node(9, head1.next)
head1.next.next.next = Node(10, head1.next.next)
head.next.next = Node(3, head.next, child=head1)
head.next.next.next = Node(4, head.next.next)
head.next.next.next.next = Node(5, head.next.next.next)
head.next.next.next.next.next = Node(6, head.next.next.next.next)



new_head = Solution().flatten(head)
print_ll(new_head)






