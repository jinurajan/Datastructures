"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
one [1,5].
"""

from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed
    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")"

def merge_intervals(intervals):
    if not intervals:
        return None
    result = []
    result.append(Interval(intervals[0].start, intervals[0].end))
    for i in range(1, len(intervals)):
        last_added_interval = result[len(result) - 1]
        cur_start = intervals[i].start
        cur_end = intervals[i].end
        prev_end = last_added_interval.end
        if cur_start <= prev_end:
            last_added_interval.end = max(cur_end, prev_end)
        else:
            result.append(Interval(cur_start, cur_end))
    return result


# Printing the list of intervals
def interval_list_to_str(lst):
    result_str = ""
    for i in range(len(lst)):
        result_str += str(lst[i]) + ", "
    return "[" + result_str[:-2] + "]"

def main():
    v1 = [Interval(1, 5), Interval(3, 7), Interval(4, 6)]
    v2 = [Interval(1, 5), Interval(4, 6), Interval(6, 8), Interval(11, 15)]
    v3 = [Interval(3, 7), Interval(6, 8), Interval(10, 12), Interval(11, 15)]
    v4 = [Interval(1, 5)]
    v6 = [Interval(1, 9), Interval(3, 8), Interval(4, 4)]
    v7 = [Interval(1, 2), Interval(3, 4), Interval(8, 8)]
    v8 = [Interval(1, 5), Interval(1, 3)]
    v9 = [Interval(1, 5), Interval(6, 9)]
    v10 = [Interval(0, 0), Interval(1, 18), Interval(1, 3)]

    all_intervals = [v1, v2, v3, v4, v6, v7, v8, v9, v10]

    for i in range(len(all_intervals)):
        print(i + 1, ". Intervals to merge: ", interval_list_to_str(all_intervals[i]), sep="")
        result = merge_intervals(all_intervals[i])
        print("   Merged intervals:\t", interval_list_to_str(result))
        print("-"*100)

if __name__ == '__main__':
    main()