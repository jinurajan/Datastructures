"""
Meeting Rooms II

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.


1. min_heap ? 
2. keep adding to min_heap if not overlapping
3. number of elements in min_heap would be the minimum number of conference rooms
"""
from typing import List

from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        min_heap = []
        heappush(min_heap, intervals[0][1])
        n = len(intervals)
        for i in range(1, n):
            if min_heap[0] <= intervals[i][0]:
                heappop(min_heap)
            heappush(min_heap, intervals[i][1])
        return len(min_heap)


from queue import PriorityQueue
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        free_rooms = 1
        q = PriorityQueue()
        intervals.sort(key=lambda x: x[0])
        q.put(intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= q.queue[0]:
                free_rooms -= 1
                q.get()    
            free_rooms += 1
            q.put(intervals[i][1])
        return free_rooms
            

