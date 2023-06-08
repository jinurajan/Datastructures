"""
Find Median from Data Stream
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.



1. use two heaps. max_heap to store the first half of the elements and min_heap to the second half
2. rebalance the heap if length of each one is more than 1 (to accomodate odd number of elements)
3. after the iteration is over the median would be the /2 of the top elements of min and max heap
"""

from heapq import *

# NOTE: Storing the extra element in the min_heap instead of max_heap
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        heappush(self.min_heap, num)
        heappush(self.max_heap, -heappop(self.min_heap))
        
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return self.min_heap[0]/2.0 + -self.max_heap[0] / 2.0
        else:
            return self.min_heap[0] / 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()