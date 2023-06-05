"""
We are given two strings, s and t, find the minimum window substring of t in s.

The minimum window substring of t in s is defined as follows:

It is the shortest substring of s that includes all of the characters present in t.

The frequency of each character in this substring that belongs to t should be equal to or greater than its frequency in t.

The order of the characters does not matter here.
"""

from collections import Counter

def is_substring(t_counter, window_counter):
    for char, count in t_counter.items():
        if window_counter[char] < count:
            return False
    return True

def min_window(s, t):
    min_window_length = float("inf")
    min_window_substring = ""
    t_counter = Counter(t)
    window_counter = Counter()
    start, end = 0, 0
    current = 0
    required = len(t_counter)
    while end < len(s):
        if s[end] in t_counter:
            window_counter[s[end]] += 1
            if window_counter[s[end]] == t_counter[s[end]]:
                current += 1
            while current == required:
                if min_window_length > end-start+1:
                    min_window_length = end-start+1
                    min_window_substring = s[start:end+1]
                if s[start] in t_counter:
                    window_counter[s[start]] -= 1
                if s[start] in t_counter and window_counter[s[start]] < t_counter[s[start]]:
                    current -= 1
                start += 1
        end += 1
    return min_window_substring

def main():
    s = ["PATTERN", "LIFE", "ABRACADABRA", "STRIKER", "DFFDFDFVD"]
    t = ["TN", "I", "ABC", "RK", "VDD"]
    for i in range(len(s)):
        print(i + 1, ".\ts: ", s[i], "\n\tt: ", t[i], "\n\tThe minimum substring containing ", \
              t[i], " is: ", min_window(s[i], t[i]), sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()