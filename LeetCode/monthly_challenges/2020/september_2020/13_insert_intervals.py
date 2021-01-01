"""
Insert Interval (Hard)
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""


def find_boundaries(intervals, val, l, r, start, end, end_point=False):
    # import pdb; pdb.set_trace()
    if l < r:
        mid = ( l + r ) / 2
        index = 1 if end_point else 0
        if (val[index] >= intervals[mid-1][index] and val[index] <= intervals[mid][index]):
            start = mid -1
            end = mid
            return start, end
        elif (val[index] >= intervals[mid][index] and val[index] <= intervals[mid+1][index]):
            start = mid
            end = mid + 1
            return start, end
        if val[index] > intervals[mid][index]:
            start = max(start, mid)
            return find_boundaries(intervals, val, mid+1, r, start, end, end_point=end_point)
        else:
            end = min(end, mid)
            return find_boundaries(intervals, val, l, mid, start, end, end_point=end_point)
    return start, end





class Solution1(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        # idea is to use binary search to find out boundaries for both a and b in terms of indexes

        """
        n = len(intervals)
        result = []
        a, b = newInterval
        st_1, st_2 = find_boundaries(
            intervals, newInterval, 0, len(intervals)-1,  -1, len(intervals))
        end_1, end_2 = find_boundaries(
            intervals, newInterval, 0, len(intervals)-1,  -1, len(intervals), end_point=True)
        print (st_1, st_2), (end_1, end_2)
        return result
        


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            # empty intervals
            return [newInterval]
        a, b = newInterval
        n = len(intervals)
        if b < intervals[0][0]:
            return [[a, b]] + intervals

        elif a > intervals[-1][1]:
            return intervals +[[a, b]]

        else:
            # lies in between
            res = []
            for i in range(len(intervals)):
                # check if a lies in between this interval
                if intervals[i][1] <  a:
                    res.append(intervals[i])
                else:
                    first = min(a, intervals[i][0])
                    last = b
                    j = i
                    while j < n and last >= intervals[j][0]:
                        last = max(intervals[j][1], last)
                        j += 1
                    res.append([first, last])
                    break
            res = res + intervals[j:]

        return res






intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval = [4,8]
print Solution().insert([[3,6], [7,9]], [1, 2]) == [[1, 2], [3, 6], [7, 9]]
print Solution().insert([[3,6], [7,9]], [1, 3]) == [[1, 6], [7,9]]

print Solution().insert([[3,6], [7,9]], [11, 12]) == [[3, 6], [7, 9], [11, 12]]
print Solution().insert([[3,6], [7,9]], [8, 12]) == [[3, 6], [7, 12]]


print Solution().insert(intervals, new_interval) == 
# print Solution().insert([[1,3],[6,9]], [2,5])

