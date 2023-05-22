"""
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

# Template for printing the linked list with forward arrows

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
            
def reverse_ll(head):
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def merge(first, second):
    head = first
    while first and second:
        new_first = first.next
        new_second = second.next
        first.next = second
        second.next = new_first
        first = new_first
        second = new_second 
    return head

def reorder_list(head):
    slow, fast = head, head
    last_node_of_first_part = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    new_head = reverse_ll(slow.next)
    slow.next = None

    return merge(head, new_head)

def main():
    input_list = [
        [1, 1, 2, 2, 3, -1, 10, 12],
        [10, 20, -22, 21, -12],
        [1, 1, 1],
        [-2, -5, -6, 0, -1, -4],
        [3, 1, 5, 7, -4, -2, -1, -6]
    ]

    for i, inp in enumerate(input_list):
        # Creating Linked Lists
        obj = LinkedList()
        obj.create_linked_list(inp)

        # Displaying original linked list
        print(i + 1, ". Original list: ", end=" ", sep="")
        print_list_with_forward_arrow(obj.head)
        print()

        # Calling the reorder_list function
        obj.head = reorder_list(obj.head)

        # Displaying modified linked list
        print("   After folding: ", end=" ")
        print_list_with_forward_arrow(obj.head)
        if i != len(input_list) - 1:
            print("\n", "-"*100, sep="")


if __name__ == '__main__':
    main()