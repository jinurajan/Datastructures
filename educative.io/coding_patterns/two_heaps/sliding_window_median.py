"""
Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

Example 1:

Input: nums=[1, 2, -1, 3, 5], k = 2
Output: [1.5, 0.5, 1.0, 4.0]
Explanation: Lets consider all windows of size ‘2’:

[1, 2, -1, 3, 5] -> median is 1.5
[1, 2, -1, 3, 5] -> median is 0.5
[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 4.0
Example 2:

Input: nums=[1, 2, -1, 3, 5], k = 3
Output: [1.0, 2.0, 3.0]
Explanation: Lets consider all windows of size ‘3’:

[1, 2, -1, 3, 5] -> median is 1.0
[1, 2, -1, 3, 5] -> median is 2.0
[1, 2, -1, 3, 5] -> median is 3.0

1. use two heaps - one for min one for max
2. for every k elements in the nums remove from left and rebalance

"""

import heapq

class SlidingWindowMedian:
    def __init__(self):
        self.min_heap, self.max_heap = [], []

    def find_sliding_window_median(self, nums, k):
        if k == 1:
            return nums
        result = []
        n = len(nums)
        left = 0
        right = 0

        def rebalance_heaps():
            if len(self.max_heap) > len(self.min_heap) + 1:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            elif len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        def add_to_heaps(num):
            if not self.max_heap or num <= -self.max_heap[0] :
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
            rebalance_heaps()

        def remove(heap,num):
            index = heap.index(num)
            heap[index] = heap[-1]
            heap.pop()
            if index < len(heap):
                heapq._siftup(heap, index)
                heapq._siftdown(heap, 0, index)

        def remove_from_heaps(num):
            if num <= -self.max_heap[0]:
                remove(self.max_heap, -num)
            else:
                remove(self.min_heap, num)

        while right < n:
            add_to_heaps(nums[right])
            if right - left + 1 == k:
                # k length sliding window
                # remove left element from heap and rebalance
                if len(self.min_heap) == len(self.max_heap):
                    result.append((self.min_heap[0] / 2.0) + (-self.max_heap[0] / 2.0))
                else:
                    result.append(-self.max_heap[0])
                remove_from_heaps(nums[left])
                rebalance_heaps()
                left += 1
            print(self.min_heap, self.max_heap)
            right += 1

        return result


def main():

      slidingWindowMedian = SlidingWindowMedian()
      result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
      print("Sliding window medians are: " + str(result))

      slidingWindowMedian = SlidingWindowMedian()
      result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
      print("Sliding window medians are: " + str(result))


main()
