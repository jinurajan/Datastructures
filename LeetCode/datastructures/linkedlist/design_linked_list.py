"""
Design Linked List
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.
"""
class LinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
   

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        node = self.head
        for i in range(index):
            if node is None:
                return -1
            node = node.next
        if node is None:
            return -1
        return node.val
            
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = LinkedListNode(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if not self.head:
            self.head = LinkedListNode(val)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = LinkedListNode(val)
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
        else:
            prev = None
            nxt = self.head
            i = 0
            while i < index and nxt is not None:
                prev = nxt
                nxt = nxt.next
                i += 1
            if i == index:
                node = LinkedListNode(val)
                prev.next = node
                node.next = nxt
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index == 0:
            if self.head:
                self.head = self.head.next
        else:
            prev = None
            nxt = self.head
            i = 0
            while i < index:
                prev = nxt
                nxt = nxt.next
                i += 1
            if i == index:
                if nxt is None:
                    # last node
                    prev.next = None
                else:
                    prev.next = nxt.next


def print_ll(node):
    if node is None:
        print "\n"
        return
    print node.val,
    node = node.next
    print_ll(node)


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
print_ll(obj.head)
obj.addAtIndex(1,2)
# print_ll(obj.head)
# print obj.get(1)
# print_ll(obj.head)
obj.deleteAtIndex(1)
print_ll(obj.head)
print obj.get(1)
print_ll(obj.head)