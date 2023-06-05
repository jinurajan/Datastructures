"""
Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]


Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10]

0 <= intervals.length <= 104
intervals[i].length == 2

0 <= starti <= endi <= pow(10, 5)
intervals is sorted by starti in ascending order.

newInterval.length == 2

0 <= start <= end <= pow(10, 5)
"""
from typing import List


import bisect


class Solution:
    def insert(self, intervals: list[list[int]],
               new_interval: list[int]) -> list[list[int]]:
        begin, end = new_interval

        left_end = bisect.bisect_left(intervals, True,
            key=lambda interval: begin <= interval[1])
        right_begin = bisect.bisect_left(intervals, True,
            key=lambda interval: end < interval[0])

        if left_end < len(intervals):
            begin = min(begin, intervals[left_end][0])
        if 0 <= right_begin-1:
            end = max(end, intervals[right_begin-1][1])

        intervals[left_end:right_begin] = [[begin, end]]
        return intervals

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        n = len(intervals)
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        merged.append(newInterval)

        while i < n:
            merged.append(intervals[i])
            i += 1
        return merged
    

    



