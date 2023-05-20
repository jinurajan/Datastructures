"""
You’re given a list of non-overlapping intervals, and you need to insert another interval into the list. Each interval is a pair of non-negative numbers, the first being the start time and the second being the end time of the interval. The input list of intervals is sorted in ascending order of start time.

The intervals in the output must also be sorted by the start time, and none of them should overlap. This may require merging those intervals that now overlap as a result of the addition of the new interval.
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
        return "[" + str(self.start) + ", " + str(self.end) \
              + "]" if self.closed else "(" + str(self.start) + ", " \
              + str(self.end) + ")"


def insert_interval(existing_intervals, new_interval):
  merged = []
  n = len(existing_intervals)
  i = 0
  while i < n and  existing_intervals[i].end < new_interval.start:
    merged.append(existing_intervals[i])
    i += 1
  while i < n and existing_intervals[i].start <= new_interval.end:
    new_interval.start = min(existing_intervals[i].start, new_interval.start)
    new_interval.end = max(existing_intervals[i].end, new_interval.end)
    i += 1
  
  merged.append(new_interval)

  while i < n:
    merged.append(existing_intervals[i])
    i += 1

  return merged


def main():
    new_interval = Interval(5, 7)
    existing_intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 8)]
    result = insert_interval(existing_intervals, new_interval)
    print([r.start, r.end] for r in result)


if __name__ == "__main__":
    main()