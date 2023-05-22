"""
Given a linked list, reverse the nodes of the linked list 
�
k
 at a time and return the modified list. Here, 
�
k
 is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of 
�
k
, the nodes left in the end will remain in their original order.

You cant alter the values of the linked list nodes. Only the nodes themselves may be changed.
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

def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value

        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")



def reverse(head, k):
  if not head:
    return
  prev, curr, next = None, head, None
  index = 0
  while curr and index < k:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    index += 1
  return prev, curr, next

def len(head):
    if not head:
        return 0
    return 1 + len(head.next)

def reverse_linked_list(head, k):
    if not k or not head:
        return head
    curr, prev, next = head, None, None
    i, count = 0, 0
    node = head
    length = len(head)
    while node:
        i += 1
        last_node_prev_k = prev
        last_node_curr_k = curr
        if i == k:
            prev, curr, next = reverse(last_node_curr_k, k)
            count += k
            if last_node_prev_k:
                last_node_prev_k.next = prev
            else:
                head = prev
            last_node_curr_k.next = curr
            if not curr or (length - count < k):
                break
            prev = last_node_curr_k
            i = 0
        node = node.next
    return head



def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8]
    input_linked_list = LinkedList()
    input_linked_list.create_linked_list(input_list)

    print("The original linked list: ", end='')
    print_list_with_forward_arrow(input_linked_list.head)
    result = reverse_linked_list(input_linked_list.head, 3)
    print("\n\nReversed linked list, with k = ", 3, ": ", sep='', end='')
    print_list_with_forward_arrow(result)


if __name__ == '__main__':
    main()


