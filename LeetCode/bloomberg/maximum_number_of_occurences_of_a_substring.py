"""
Maximum Number of Occurrences of a Substring

Given a string s, return the maximum number of occurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.
"""
from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
        number of unique chars in substring must be less than or equal to maxLetters
        
        minsize <= len(substring) <= maxSize
        
        counter to find the frequency of a substring
        
        sliding window of size minSize and upto maxSize to find the substring
        """
        
        counter = Counter()
        max_count = 0
        start = 0
        end = 0
        
        substring_counter = Counter()
        n = len(s)
        while end < n:
            counter[s[end]] += 1
            while end-start+1 > minSize:
                if counter[s[start]] == 1:
                    del counter[s[start]]
                else:
                    counter[s[start]] -= 1
                start += 1
            if end - start + 1 == minSize and len(counter) <= maxLetters:
                substring_counter[s[start:end+1]] += 1
            max_count = max(max_count, substring_counter[s[start:end+1]])
            end += 1
        
        return max_count
