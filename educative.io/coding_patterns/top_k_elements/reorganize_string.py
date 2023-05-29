"""
Given a string, rearrange it so that any two adjacent characters are not the same. If such a reorganization of the characters is possible, output any possible valid arrangement. Otherwise, return an empty string.

Constraints:

1≤input_string.length ≤ 500
Input string consists of lowercase English letters.
"""


# importing libraries
from collections import Counter
from heapq import *

def reorganize_string(input_string):
    max_heap = []
    char_counter = Counter(input_string)
    for char,count in char_counter.items():
        max_heap.append((-count, char))
    heapify(max_heap)
    result = ""
    prev = None
    while max_heap or prev:
        if prev and len(max_heap) == 0:
            return ""
        count, char = heappop(max_heap)
        result += char
        count += 1
        if prev:
            heappush(max_heap, prev)
            prev = None
    
        if count != 0:
            prev = (count, char)
    return result


# Driver code
def main():
    test_cases = ["programming", "hello", "fofjjb",
                  "abbacdde", "aba", "awesome", "aaab"]
    for i in range(len(test_cases)):
        print(i+1, '. \tInput string: "', test_cases[i], '"', sep="")
        temp = reorganize_string(test_cases[i])
        print('\tReorganized string: "', temp + '"' if temp else '"', sep="")
        print("-"*100)


if __name__ == '__main__':
    main()