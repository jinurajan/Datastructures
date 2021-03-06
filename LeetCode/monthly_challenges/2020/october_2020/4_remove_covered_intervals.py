"""
Remove Covered Intervals

Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
Example 3:

Input: intervals = [[0,10],[5,12]]
Output: 2
Example 4:

Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2
Example 5:

Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= intervals[i][0] < intervals[i][1] <= 10^5
All the intervals are unique.
"""
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:   return 0
        n = len(intervals)
        if n == 1:
            return 0
        count = 1
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        init = intervals[0]
        for i in range(1, n):
            if init[1] < intervals[i][1]:
                count += 1
                init = [min(init[0], intervals[i][0]), max(intervals[i][1], init[1])]
        return count

print(Solution().removeCoveredIntervals([[0,10],[5,12]])) # 2 
print(Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]))   # 2
print(Solution().removeCoveredIntervals([[3,10],[4,10],[5,11]])) # 2
print(Solution().removeCoveredIntervals([[1,2],[1,4],[3,4]])) # 1
