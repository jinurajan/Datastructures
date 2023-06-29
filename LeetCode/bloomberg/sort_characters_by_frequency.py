"""
 Sort Characters By Frequency

 
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
"""
from collections import defaultdict

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        result = ""
        for char, freq in counts.most_common():
            result += char * freq
        return result

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        freq_counter = defaultdict(list)
        max_count = 0
        for char, count in counter.items():
            max_count = max(max_count, count)
            freq_counter[count].append(char)
        result = ""
        for i in range(max_count, 0, -1):
            for char in freq_counter[i]:
                result += char * i
        return result


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        max_freq = max(counts.values())
        buckets = [[] for _ in range(max_freq+1)]
        for char, count in counts.items():
            buckets[count].append(char)
        result = ""
        for i in range(max_freq, 0, -1):
            for char in buckets[i]:
                result += char * i
        return result