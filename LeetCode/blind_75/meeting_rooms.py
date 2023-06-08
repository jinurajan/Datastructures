"""
Meeting Rooms


Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

intervals = [[0,30],[5,10],[15,20]]
"""

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        start, end = intervals[0]
        for i in range(1, n):
            if intervals[i][0] < end:
                return False
            start, end = intervals[i]
        return True
    
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        n = len(intervals)
        for i in range(n-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True