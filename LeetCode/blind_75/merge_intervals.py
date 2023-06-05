"""
Merge Intervals


Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by starting time
        intervals = sorted(intervals, key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= result[-1][1]:
                # overlapping
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start, end])
        return result