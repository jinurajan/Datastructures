"""
Find the kth largest element in an unsorted array.
"""

from heapq import *
def find_kth_largest(arr, k):
    min_heap = []
    for ele in arr:
        heappush(min_heap, ele)
        if len(min_heap) > k:
            heappop(min_heap)
    return heappop(min_heap)


def find_kth_largest(array, k):
    # space efficient
    k_numbers_min_heap = []
    # Put first k elements in the min heap
    for i in range(k):
        k_numbers_min_heap.append(array[i])
        # heappush(min_heap, array[i])
    heapify(k_numbers_min_heap)
    # Go through the remaining elements of the list, if the element from the list is greater than the
    # top(smallest) element of the heap, remove the top element from heap and add the element from array
    for i in range(k, len(array)):
        if array[i] > k_numbers_min_heap[0]:
            heappop(k_numbers_min_heap)
            heappush(k_numbers_min_heap, array[i])
    # The root of the heap has the Kth largest element
    return k_numbers_min_heap[0]



# Driver code
def main():
    input_list = [[1, 5, 12, 2, 11, 9, 7, 30, 20], [23, 13, 17, 19, 10], [3, 2, 5, 6, 7], [1, 4, 6, 0, 2], [1, 2, 3, 4, 5, 6, 7]]
    k_list = [3, 4, 5, 1, 7]
    for i in range(len(input_list)):
        print(i + 1, ".\tInput array: ", input_list[i], ", k: ", k_list[i], sep="")
        print("\tkth largest number: ", find_kth_largest(input_list[i], k_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()