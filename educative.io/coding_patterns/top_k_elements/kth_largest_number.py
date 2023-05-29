"""
Given an infinite stream of integers, nums, design a class to find the kth largest element in a stream.
"""

from heapq import *

class KthLargest:
    # constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.min_heap = nums
        self.k = k
        heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heappop(self.min_heap)


    # adds element in the heap
    def add(self, val):
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.return_Kth_largest()
        
    # returns kth largest element from heap
    def return_Kth_largest(self):
        return self.min_heap[0]
    

def main():
    nums = [3, 6, 9, 10]
    temp = [3, 6, 9, 10]
    print("Initial stream: ", nums, sep = "")
    print("k: ", 3, sep = "")
    KLargest = KthLargest(3, nums)
    val = [4, 7, 10, 8, 15]
    print()
    for i in range(len(val)):
        print("\tAdding a new number ", val[i], " to the stream", sep = "")
        temp.append(val[i])
        print("\tNumber stream: ", temp, sep = "")
        print("\tKth largest element in the stream: ", KLargest.add(val[i]))
        print("-"*100)


if __name__ == "__main__":
    main()
