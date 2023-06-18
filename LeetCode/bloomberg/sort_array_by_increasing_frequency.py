"""
Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
"""
from typing import List
from collections import defaultdict

from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return sorted(nums, key=lambda x: (counter[x], -x))

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums).most_common()
        counter.sort(key=lambda x: (x[1], -x[0]))

        result = []
        for entry in counter:
            val, freq = entry
            result.extend([val]*freq)

        return result


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums).most_common()
        counter.sort(key=lambda x: x[0], reverse=True)
        counter.sort(key=lambda x: x[1])

        result = []
        for entry in counter:
            val, freq = entry
            result.extend([val]*freq)

        return result


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result = []
        # {3: 1, 2: 3, 1: 2}
        counter = Counter(nums)
        # {1: [3], 2: [1], 3: [2]}
        freq_map = defaultdict(list)
        for num, count in counter.items():
            freq_map[count].append(num)
        for freq in sorted(freq_map.keys()):
            values = sorted(freq_map[freq], reverse=True)
            for val in values:
                for i in range(freq):
                    result.append(val)
        return result