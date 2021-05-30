"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
"""

from heapq import *

def find_k_largest_numbers(nums, k):
  return nlargest(k, nums)


def find_k_largest_numbers(nums, k):
  minHeap = []
  # put first 'K' numbers in the min heap
  for i in range(k):
    heappush(minHeap, nums[i])

  # go through the remaining numbers of the array, if the number from the array is bigger than the
  # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if nums[i] > minHeap[0]:
      heappop(minHeap)
      heappush(minHeap, nums[i])

  # the heap has the top 'K' numbers, return them in a list
  return list(minHeap)



def find_k_largest_numbers(nums, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, nums[i])

    for j in range(k, len(nums)):
        if min_heap[0] < nums[j]:
            heappop(min_heap)
            heappush(min_heap, nums[j])

    return list(min_heap)

def main():

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

  print("Here are the top K numbers: " +
        str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()