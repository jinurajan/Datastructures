"""
For two lists of closed intervals given as input, interval_list_a and interval_list_b, where each interval has its own start and end time, write a function that returns the intersection of the two interval lists.

For example, the intersection of [3,8] [5,10] [5,10] is [5,8]
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
        return "[" + str(self.start) + ", " + str(self.end) + "]" if self.closed else "(" + str(self.start) + ", " + str(self.end) + ")"


def display(vec):
    string = "["

    if vec:
        for i in range(len(vec)):
            string += str(vec[i])
            if i + 1 < len(vec):
                string += ", "

    string += "]"

    return string

# Function to find the intersecting points between two intervals
def intervals_intersection(interval_list_a, interval_list_b):
    intersections = []
    i, j = 0, 0
    while i < len(interval_list_a) and j < len(interval_list_b):
        start = max(interval_list_a[i].start, interval_list_b[j].start)
        end = min(interval_list_a[i].end, interval_list_b[j].end)
        if start <= end:
            intersections.append(Interval(start, end))
        if interval_list_a[i].end <= interval_list_b[j].end:
            i += 1
        else:
            j += 1
    return intersections
        
