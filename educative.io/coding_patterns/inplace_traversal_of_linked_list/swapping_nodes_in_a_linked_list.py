"""
Given the linked list and an integer 
�
k
, return the head of the linked list after swapping the values of the 
�
�
ℎ
k 
th
 
 node from the beginning and the 
�
�
ℎ
k 
th
 
 node from the end of the linked list.

"""

# Template for linked list node class

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None
    
    # insert_node_at_head method will insert a LinkedListNode at 
    # head of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    
    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method. 
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result



            
def swap_nodes(head, k):
    # find kth node
    slow = head
    fast = head
    i = 1
    while i < k:
        fast = fast.next
        i += 1
    first_kth_node = fast
    while fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next
    
    # kth node from other side will be slow
    last_kth_node = slow
    
    temp = first_kth_node.data
    first_kth_node.data = last_kth_node.data
    last_kth_node.data = temp

    return head
