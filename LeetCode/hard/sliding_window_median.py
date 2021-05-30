"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation:
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6

"""

import heapq


class Solution:
    def __init__(self):
        self.max_heap, self.min_heap = [], []

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums
        n = len(nums)
        left = 0
        right = 0

        def rebalance_heaps():
            if len(self.max_heap) > len(self.min_heap) + 1:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            elif len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

        def add_to_heap(num):
            if not self.max_heap or num <= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
            rebalance_heaps()

        def remove(heap, num):
            index = heap.index(num)
            heap[index] = heap[-1]
            heap.pop()
            if index < len(heap):
                heapq._siftup(heap, index)
                heapq._siftdown(heap, 0, index)

        def remove_from_heap(num):
            if num <= -self.max_heap[0]:
                remove(self.max_heap, -num)
            else:
                remove(self.min_heap, num)
            rebalance_heaps()

        result = []
        while right < n:
            add_to_heap(nums[right])
            if right - left + 1 == k:
                if len(self.min_heap) == len(self.max_heap):
                    result.append((self.min_heap[0] / 2.0) + (-self.max_heap[0] / 2.0))

                else:
                    result.append(-self.max_heap[0])
                remove_from_heap(nums[left])
                left += 1
            right += 1
        return result
