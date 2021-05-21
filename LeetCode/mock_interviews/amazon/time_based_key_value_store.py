"""
Time Based Key-Value Store

Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


 Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:
TimeMap kv;
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
kv.get("foo", 1);  // output "bar"
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // output "bar2"
kv.get("foo", 5); //output "bar2"

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]


Note:

All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
"""


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_times = {}  # data_times = { key1: { time1: value1, time2: valuex...}
        self.keys_times = {}  # keys_times = { key1: [time1,time2,...]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data_times:
            self.data_times[key] = {}
        self.data_times[key][timestamp] = value
        if key not in self.keys_times:
            self.keys_times[key] = [timestamp]
        else:
            if timestamp > self.keys_times[key][-1]:
                self.keys_times[key].append(timestamp)
                return
            first, last = 0, len(self.keys_times[key])
            while first <= last:
                mid = (first + last) // 2
                if self.keys_times[key][mid] > timestamp:
                    if self.keys_times[key][mid - 1] < timestamp:
                        self.keys_times[key].insert(mid - 1)
                        break
                    last = mid - 1
                else:
                    if self.keys_times[key][mid + 1] < timestamp:
                        self.keys_times[key].insert(mid)
                        break
                    first = mid + 1

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.keys_times.get(key, None)
        if timestamp < timestamps[0]:
            return ""
        if timestamp > timestamps[-1]:
            return self.data_times[key][timestamps[-1]]
        if timestamps is None:
            return ""

        first, last = 0, len(timestamps) - 1
        while first <= last:
            mid = (first + last) // 2
            if timestamps[mid] == timestamp:
                return self.data_times[key][timestamps[mid]]
            elif timestamps[mid] > timestamp:
                if timestamps[mid - 1] < timestamp:
                    return self.data_times[key][timestamps[mid - 1]]
                last = mid - 1
            else:
                if timestamps[mid + 1] > timestamp:
                    return self.data_times[key][timestamps[mid]]
                first = mid + 1

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)