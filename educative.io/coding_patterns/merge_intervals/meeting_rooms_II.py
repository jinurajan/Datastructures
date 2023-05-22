"""
We are given an input array of meeting time intervals, intervals, where each interval has a start time and an end time. Your task is to find the minimum number of meeting rooms required to hold these meetings.

1 <= intervals.length <= pow(10, 4)

0 <= start < end < pow(10, 6)
"""
from interval import Interval
import heapq

def find_sets(intervals):
    # Your code will replace this placeholder return statement
    if not intervals:
        return 0
    min_heap = []
    intervals = sorted(intervals, key=lambda x: x.start)
    heapq.heappush(min_heap, intervals[0].end)
    for i in range(1, len(intervals)):
        if min_heap[0] <= intervals[i].start:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, intervals[i].end)
    return len(min_heap)
