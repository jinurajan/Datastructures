"""
Top K Frequent Words

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

"""
from typing import List
from heapq import *
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counter = Counter(words)
        max_heap = []
        for word, count in word_counter.items():
            heappush(max_heap, (-count, word))
        
        result = []
        for i in range(k):
            result.append(heappop(max_heap)[1])
        
        return result
            