"""
Given an m number of sorted lists in ascending order and an integer, k, find the kth smallest number among all the given lists.

Although there can be repeating values in the lists, each element is considered unique and, therefore, contributes to calculating the  kth smallest element.

If k is greater than the total number of elements in the input lists, return the greatest element from all the lists and if there are no elements in the input lists, return 0.

"""

from heapq import *


def k_smallest_number(lists, k):
    min_heap = []
    for idx,l in enumerate(lists):
        if l:
            heappush(min_heap,(l[0], idx, 0))
    pop_count = 0
    min_ele = 0
    while min_heap:
        min_ele, parent_idx, idx = heappop(min_heap)
        pop_count += 1
        if pop_count == k:
            break
        if idx < len(lists[parent_idx]) - 1:
            heappush(min_heap, (lists[parent_idx][idx+1], parent_idx, idx+1))

    return min_ele


# driver code
def main():
    # multiple inputs for efficient results
    lists = [[[2, 6, 8], [3,6,10], [5, 8, 11]],
             [[1, 2, 3], [4, 5], [6, 7, 8, 15], [10, 11, 12, 13], [5, 10]],
             [[], [], []],
             [[1, 1, 3, 8], [5, 5, 7, 9], [3, 5, 8, 12]],
             [[5, 8, 9, 17], [], [8, 17, 23, 24]]]

    k = [5, 50, 7, 4, 8]

    # loop to execute till the length of list k
    for i in range(len(k)):
        print(i + 1, ".\t Input lists: ", lists[i],
              f"\n\t K = {k[i]}",
              f"\n\t {k[i]}th smallest number from the given lists is: ",
              k_smallest_number(lists[i], k[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
