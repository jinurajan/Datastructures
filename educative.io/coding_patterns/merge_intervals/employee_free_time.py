"""
You’re given a list containing the schedules of multiple people. Each person’s schedule is a list of non-overlapping intervals in sorted order. An interval is specified with the start time and the end time, both being positive integers. Your task is to find the list of intervals representing the free time for all the people. We’re not interested in the interval from negative infinity to zero or from the end of the last scheduled interval in the input to positive infinity.

1 ≤ schedule.length , schedule[i].length ≤ 50

0 ≤ interval.start < interval.end ≤ pow(10, 8) where interval is any interval in the list of schedules.
Every interval is guaranteed to have a non-zero duration.

"""
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


def employee_free_time(schedule):
    if not schedule:
        return [] 
    result = []
    intervals = []
    for i, each_interval_list in enumerate(schedule):
        intervals.extend(each_interval_list)
    intervals = sorted(intervals, key=lambda x: x.start)
    prev_end = intervals[0].end
    for i in range(1, len(intervals)):
        if prev_end < intervals[i].start:
            result.append(Interval(prev_end, intervals[i].start))
        prev_end = max(prev_end, intervals[i].end)
    return result