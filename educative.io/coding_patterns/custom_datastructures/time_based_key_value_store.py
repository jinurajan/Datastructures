"""
Time based key value store

Implement a data structure that can store multiple values of the same key at different timestamps and retrieve the key’s value at a certain timestamp.


You will need to implement the TimeStamp class. This class has the following functions:

Init(): This function initializes the values dictionary and timestamp dictionary.
Set Value(key, value, timestamp): This function stores the key and value at any given timestamp.

Get Value(key, timestamp): This function returns the value set for this key at the specified timestamp

Note:  When a query requests the value of a key at a timestamp that is more recent than the most recent entry for that key, our data structure should return the value corresponding to the most recent timestamp.
"""


import random


class TimeStamp:
    def __init__(self):
        self.values_dict = {}
        self.timestamps_dict = {}

    #  Set TimeStamp data variables
    def set_value(self, key, value, timestamp):
        if key in self.values_dict:
            if timestamp < self.timestamps_dict[key][-1]:
                value = self.timestamps_dict[key][-1]
            elif value != self.values_dict[key][len(self.values_dict[key])-1]:
                self.values_dict[key].append(value)
                self.timestamps_dict[key].append(timestamp)
        else:
            self.values_dict[key] = [value]
            self.timestamps_dict[key] = [timestamp]

    def search_index(self, n, key, timestamp):
        left = 0
        j = right = n
        mid = 0

        while left < right:
            mid = (left+right) // 2
            if self.timestamps_dict[key][mid] <= timestamp:
                left = mid+1
            else:
                right = mid
        return left-1


    # Get TimeStamp data variables
    def get_value(self, key, timestamp):
        if key not in self.values_dict:
            return ""
        index = self.search_index(
            len(self.timestamps_dict[key]),
            key,
            timestamp)
        if index > -1:
            return self.values_dict[key][index]
        return ""


from collections import defaultdict
from bisect import bisect_right


class TimeStamp:
    def __init__(self):
        self.values_dict = {}
        self.timestamps_dict = {}

    #  Set TimeStamp data variables
    def set_value(self, key, value, timestamp):
        if key in self.values_dict:
            if timestamp < self.timestamps_dict[key][-1]:
                value = self.timestamps_dict[key][-1]
            elif value != self.values_dict[key][len(self.values_dict[key])-1]:
                self.values_dict[key].append(value)
                self.timestamps_dict[key].append(timestamp)
        else:
            self.values_dict[key] = [value]
            self.timestamps_dict[key] = [timestamp]

    # Get TimeStamp data variables
    def get_value(self, key, timestamp):
        if key not in self.values_dict:
            return ""
        index = bisect_right(self.timestamps_dict[key], timestamp)-1
        if index > -1:
            return self.values_dict[key][index]
        return ""



# Driver code
def main():
    ts = TimeStamp()
    num = 1
    random_value = 0
    input = (
            ("course", "OOP", 3),
            ("course", "PF", 5),
            ("course", "OS", 7),
            ("course", "ALGO", 9),
            ("course", "DB", 10)
        )

    for i in input:
        print(num, ".\tAdd value: (", '"', i[0], '"',
                   ", ", '"', i[1], '"', ", ", i[2], ")", sep="")
        ts.set_value(i[0], i[1], i[2])
        random_value = random.randint(0, 10)
        print("\n\tGet value for:")
        print("\t\tKey = course  \n\t\tTimestamp = ", random_value, sep="")
        print("\n\tReturned value = ", '"',
              ts.get_value("course", random_value), '"', sep="")
        num += 1
        print("-" * 100, sep="")


if __name__ == "__main__":
    main()