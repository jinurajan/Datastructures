"""
Find the kth smallest element in an (n×n) matrix, where each row and column of the matrix is sorted in ascending order.
Although there can be repeating values in the matrix, each element is considered unique and, therefore, contributes to calculating the kth smallest element.
"""


from heapq import *

def kth_smallest_element(matrix, k):
    min_heap = []
    smallest_ele = None
    popped_count = 0
    rows = len(matrix)
    for i in range(rows):
        heappush(min_heap, (matrix[i][0], i, 0))
    while min_heap:
        smallest_ele, row_id, idx = heappop(min_heap)
        popped_count += 1
        if popped_count == k:
            break
        if idx < len(matrix[row_id])-1:
            heappush(min_heap, (matrix[row_id][idx+1], row_id, idx+1))
    return smallest_ele



# driver code
def main():

    # multiple inputs for efficient results
    matirx = [
        [[2, 6, 8],
         [3, 7, 10],
         [5, 8, 11]],

        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],

        [[5]],

        [[1, 1, 3, 8],
         [5, 5, 7, 9],
         [3, 5, 8, 12]],

        [[2, 2, 6, 6, 8, 9],
         [1, 4, 7, 10, 10, 22],
         [5, 7, 9, 11, 13, 15],
         [44, 55, 66, 77, 88, 99]]
    ]

    k = [3, 4, 1, 12, 8]

    # loop to execute till the length of list k
    for index in range(len(k)):
        print(index + 1, ".\t Input matrix: ",
              matirx[index], f"\n\t k = {k[index]}", sep="")
        print("\t Kth smallest number in the matrix is: ",
              kth_smallest_element(matirx[index], k[index]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
