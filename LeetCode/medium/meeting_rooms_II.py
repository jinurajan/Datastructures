"""

"""
from typing import List

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        free_rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(free_rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if free_rooms[0] <= intervals[i][0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, intervals[i][1])
        return len(free_rooms)


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


