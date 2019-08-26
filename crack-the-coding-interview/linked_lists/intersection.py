class LinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def print_ll(head):

    while head is not None:
        print head.data,
        head = head.next
        if head is not None:
            print "->",


def length(node):
    current = node
    count = 0
    while current is not None:
        count = count + 1
        current = current.next
    return count


def IsIntersecting(ll_1, ll_2):
    len1 = length(ll_1)
    len2 = length(ll_2)

    shorter = ll_1 if len1 < len2 else ll_2
    longer = ll_1 if len1 > len2 else ll_2

    diff = len1 - len2 if len1 > len2 else len2 - len1
    count = 0
    while count < diff:
        count += 1
        longer = longer.next
    # now both lls are of same length
    return Intersection(shorter, longer)


def Intersection(ll_1, ll_2):
    while ll_1 != ll_2:
        ll_1 = ll_1.next
        ll_2 = ll_2.next
    return ll_1

if __name__ == "__main__":
    ll_1 = LinkedListNode(3)
    ll_1.next = LinkedListNode(5)
    ll_1.next.next = LinkedListNode(2)
    ll_1.next.next.next = LinkedListNode(1)
    ll_1.next.next.next.next = LinkedListNode(7)
    ll_1.next.next.next.next.next = LinkedListNode(8)
    ll_1.next.next.next.next.next.next = LinkedListNode(9)

    ll_2 = LinkedListNode(3)
    ll_2.next = LinkedListNode(2)
    ll_2.next.next = ll_1.next.next.next

    print IsIntersecting(ll_1, ll_2).data
