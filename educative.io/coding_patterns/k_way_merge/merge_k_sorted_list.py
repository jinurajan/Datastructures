"""
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
Example 2:

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
"""
from __future__ import print_function
from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def merge_two_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    dummy_head = ListNode(-1)
    node = dummy_head
    while l1 and l2:
        if l1.value <= l2.value:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    if l1:
        node.next = l1
    if l2:
        node.next = l2
    return dummy_head.next


def merge_lists_1(lists):
    total = len(lists)
    interval = 1
    while interval < total:
        for i in range(0, total - interval, interval * 2):
            lists[i] = merge_two_lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if total > 0 else None

    return resultHead


def merge_lists(lists):
    min_heap = []
    for head in lists:
        if head:
            heappush(min_heap, head)

    dummy_head = ListNode(-1)
    new_node = dummy_head
    while min_heap:
        node = heappop(min_heap)
        new_node.next = node
        new_node = new_node.next
        if node.next:
            heappush(min_heap, node.next)
    return dummy_head.next


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next


main()

