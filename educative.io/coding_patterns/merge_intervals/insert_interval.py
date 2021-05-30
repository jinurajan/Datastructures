"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
"""


def insert(intervals, new_interval):
    merged = []
    n = len(intervals)
    i = 0
    while i < n and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1

    merged.append(new_interval)

    while i < n:
        merged.append(intervals[i])
        i += 1

    return merged


def main():
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
