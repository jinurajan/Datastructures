
class CircularLLNode(object):
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None


class CircularLL(object):
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = CircularLLNode(data)
        else:
            node = self.head
            prev = None
            while node.next is not None:
                prev = node
                node = node.next
            new_node = CircularLLNode(data)
            new_node.prev = prev
            node.next = new_node

    def remove(self, data):
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                if prev is None:
                    # head has to be deleted
                    if current.next is None:
                        # single element in LL
                        self.head = None
                    else:
                        self.head = current.next
                        current.next.prev = None
                elif current.next is None:
                    # tail node
                    prev.next = None
                else:
                    # not the first node
                    prev.next = current.next
                    current.next.prev = prev
                return
            else:
                prev = current
                current = current.next

    def print_ll(self, head):
        current = head
        while current is not None:
            print current.data,
            if current.next is not None:
                print "->",
            current = current.next
        print "\n"


if __name__ == "__main__":
    ll = CircularLL()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.print_ll(ll.head)
    # remove middle node
    ll.remove(2)
    ll.print_ll(ll.head)
    # remove head node
    ll.remove(1)
    ll.print_ll(ll.head)
    ll.remove(4)
    ll.print_ll(ll.head)
    ll.remove(3)
    ll.print_ll(ll.head)
