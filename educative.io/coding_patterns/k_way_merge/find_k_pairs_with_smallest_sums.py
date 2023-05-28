"""
"""

from heapq import *


def k_smallest_pairs(list1, list2, k):
    if len(list1) < len(list2):
        list1, list2 = list2, list1
    result = []
    min_heap = []
    pop_count = 0
    for i in range(len(list2)):
        heappush(min_heap, (list1[0]+list2[i], 0, i))
    while min_heap:
        _, l1, l2 = heappop(min_heap)
        result.append([list1[l1], list2[l2]])
        pop_count += 1
        if pop_count == k:
            break
        if l1+1 < len(list1):
            heappush(min_heap, (list1[l1+1]+list2[l2], l1+1, l2))

    return result


# driver code
def main():

    # multiple inputs for efficient results
    list1 = [[2, 8, 9],
             [1, 2, 300],
             [1, 1, 2],
             [4, 6],
             [4, 7, 9],
             [1, 1, 2]]

    # multiple inputs for efficient results
    list2 = [[1, 3, 6],
             [1, 11, 20, 35, 300],
             [1, 2, 3],
             [2, 3],
             [4, 7, 9],
             [1]]

    k = [9, 30, 1, 2, 5, 4]

    # loop to execute till the length of list k
    for i in range(len(k)):
        print(i + 1, ".\t Input pairs: ", list1[i], ", ", list2[i],
              f"\n\t k = {k[i]}", sep="")
        print("\t Pairs with the smallest sum are: ",
              k_smallest_pairs(list1[i], list2[i], k[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
