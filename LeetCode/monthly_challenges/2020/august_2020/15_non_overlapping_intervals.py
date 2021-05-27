"""
Non-overlapping Intervals
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

"""
import sys


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: x[1])
        counter = 0
        max_interval = -sys.maxint
        for interval in intervals:
            if interval[0] >= max_interval:
                counter += 1
                max_interval = interval[1]
        return len(intervals) - counter


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # sort by starting point
        intervals = sorted(intervals, key=lambda x: x[1])
        n = len(intervals)
        prev = count = 0
        end = intervals[0][1]
        count = 1
        for i in range(1, n):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1
        return n - count


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # sort by starting point
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        prev = count = 0
        for i in range(1, n):
            if intervals[prev][1] > intervals[i][0]:
                if intervals[prev][1] > intervals[i][1]:
                    prev = i
                # non overlapping
                count += 1
            else:
                prev = i
        return count


print Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
print Solution().eraseOverlapIntervals([[1,2],[2,3]]) == 0
print Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
print Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]) == 2