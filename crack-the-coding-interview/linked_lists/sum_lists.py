"""
Sum Lists: You have two numbers represented by a linked list,where each node contains a single digit. The digits are stored in reverse order,such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the summation as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295. Output:2 -> 1 -> 9.Thatis,912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295. Output:9 ->1 ->2.Thatis,912.
"""


def add_list(ll_1, ll_2, carry):
    # print ll_1.data, ll_2.data, carry
    if ll_1 is None and ll_2 is None and carry == 0:
        return None
    value = carry
    if ll_1 is not None:
        value += ll_1.data
    if ll_2 is not None:
        value += ll_2.data

    remainder = value % 10
    result = LinkedListNode(remainder)

    if ll_1 is not None or ll_2 is not None:
        more = add_list(
            None if ll_1 is None else ll_1.next,
            None if ll_2 is None else ll_2.next,
            1 if value >= 10 else 0)
        result.next = more

    return result


def summation_list_reverse_order(ll_1, ll_2):
    head_1 = ll_1
    head_2 = ll_2
    result_start = None
    result_end = None
    quotient = 0
    len1 = length(ll_1)
    len2 = length(ll_2)
    if len1 > len2:
        padListAttheEnd(ll_2, len1 - len2)
    else:
        padListAttheEnd(ll_1, len2 - len1)
    while head_1 is not None or head_2 is not None:
        summation_val = head_1.data + head_2.data
        summation_val = summation_val + quotient
        remainder = summation_val % 10

        if result_start is None:
            # head
            result_start = LinkedListNode(remainder)
            result_end = result_start
        else:
            result_end.next = LinkedListNode(remainder)
            result_end = result_end.next
        quotient = summation_val / 10

        head_1 = head_1.next
        head_2 = head_2.next

    return result_start


def length(llist):
    head = llist
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


class PartialSum(object):
    def __init__(self):
        self.sum = None
        self.carry = 0


def addListForward(ll_1, ll_2):
    len1 = length(ll_1)
    len2 = length(ll_2)
    if len1 > len2:
        ll_2 = padList(ll_2, len1 - len2)
    else:
        ll_1 = padList(ll_1, len2 - len1)

    summation = addListHelper(ll_1, ll_2)
    if summation.carry == 0:
        return summation.sum
    else:
        result = insertBefore(summation.summation, summation.carry)
        return result


def addListHelper(ll_1, ll_2):
    if ll_1 is None and ll_2 is None:
        summation = PartialSum()
        return summation
    summation = addListHelper(ll_1.next, ll_2.next)
    val = summation.carry + ll_1.data + ll_2.data

    full_result = insertBefore(summation.sum, val % 10)
    summation.sum = full_result
    summation.carry = val / 10
    return summation


def insertBefore(llist, val):
    node = LinkedListNode(val)
    if llist is not None:
        node.next = llist
    return node


def padListAttheEnd(head, padding):
    current = head
    while current.next is not None:
        current = current.next

    count = 0
    while count < padding:
        count += 1
        new_node = LinkedListNode(0)
        current.next = new_node


def padList(head, padding):
    count = 0
    while count < padding:
        count += 1
        new_node = LinkedListNode(0)
        new_node.next = head
        head = new_node
    return head


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

if __name__ == "__main__":
    ll_1 = LinkedListNode(1)
    ll_1.next = LinkedListNode(2)
    ll_1.next.next = LinkedListNode(3)
    ll_1.next.next.next = LinkedListNode(4)
    print_ll(ll_1)
    print "+",
    ll_2 = LinkedListNode(5)
    ll_2.next = LinkedListNode(6)
    ll_2.next.next = LinkedListNode(7)
    print_ll(ll_2)
    print "=",
    result_ll = summation_list_reverse_order(ll_1, ll_2)
    print_ll(result_ll)
    print "\n"
    result_ll_1 = add_list(ll_1, ll_2, 0)
    print "1 -> 2 -> 3 -> 4 + 5 -> 6 -> 7 =",
    print_ll(result_ll_1)
    print "\n"
    print "FOLLOW UP: forward order"
    ll_1 = LinkedListNode(1)
    ll_1.next = LinkedListNode(2)
    ll_1.next.next = LinkedListNode(3)
    ll_1.next.next.next = LinkedListNode(4)
    print_ll(ll_1)
    print "+",
    ll_2 = LinkedListNode(5)
    ll_2.next = LinkedListNode(6)
    ll_2.next.next = LinkedListNode(7)
    print_ll(ll_2)
    print "=",
    result = addListForward(ll_1, ll_2)
    print_ll(result)
