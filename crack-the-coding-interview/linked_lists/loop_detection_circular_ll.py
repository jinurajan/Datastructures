
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

    def print_ll(self):
        current = self.head
        while current is not None:
            print current.data,
            if current.next is not None:
                print "->",
            current = current.next
        print "\n"

    def detect_loop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                break
        if fast_ptr is None or fast_ptr.next is None:
            # no meeting point
            return None

        slow_ptr = self.head
        while slow_ptr != fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        return fast_ptr

if __name__ == "__main__":
    ll = CircularLL()
    ll.add("A")
    ll.add("B")
    ll.add("C")
    ll.add("D")
    ll.add("E")

    ll.head.next.next.next.next.next = ll.head.next.next
    print ll.detect_loop().data
