"""
You’re given a linked list. Your task is to reverse all of the nodes that are present in the groups with an even number of nodes in them. The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers 
(1,2,3,4...). The length of a group is the number of nodes assigned to it. In other words:

- the first node is assigned to first group
- the second and third node is assigned to second group and hence should be reversed
- the fourth, fifth and sixth node is assigned to third group 

and so on

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

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
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

def reverse_even_length_groups(head):
    prev = head # since first group is not reversed
    group_no = 2 # start with 2 and then increment

    while prev.next:
        node = prev
        n = 0
        for i in range(group_no):
            if not node.next:
                break
            n += 1
            node = node.next
        # there are enough nodes for the group_no
        if n % 2 == 0:
            # reverse this part from prev to node
            reverse = node.next
            curr = prev.next
            for j in range(n):
                nxt = curr.next
                curr.next = reverse
                reverse = curr
                curr = nxt
            prev_next = prev.next
            prev.next = node
            prev = prev_next
        else:
            # odd number. ignore this section
            prev = node
        group_no += 1
    return head


def main():
    input = [
        [1, 2, 3, 4],
        [10, 11, 12, 13, 14],
        [15],
        [16, 17]
    ]

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(
            i+1, ".\tIf we reverse the even length groups of the linked list: ", end='\n\t')
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\n\tWe will get: ", end='\n\t')
        print_list_with_forward_arrow(
            reverse_even_length_groups(input_linked_list.head))
        print("\n")
        print("-" * 100)


if __name__ == '__main__':
    main()
