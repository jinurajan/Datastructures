"""
Maximum Number of Non-Overlapping Substrings

Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l], either j < k or i > l is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.


Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.


Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.


"""

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        char_map = defaultdict(list)
        for i, char in enumerate(s):
            if char not in char_map:
                char_map[char] = [i, i]
            else:
                char_map[char][1] = i
        intervals = char_map.values()
        intervals = sorted(intervals, key=lambda x: x[1])
        print(intervals)
        n = len(intervals)
        dp = [1 for i in range(n)]
        start = intervals[0]
        for i in range(1, n):
            if intervals[i][0] > start[1]:
                # non overlapping
                dp[i] = dp[ i -1] + 1
            else:
                # overlapping
                dp[i] = max(dp[ i -1 ] -1, dp[i])
        print(dp)
        result = []
        seen = set()
        prev = dp[0]
        min_index = intervals[0][0]
        max_index = intervals[0][1]
        for i in range(1, n):
            print("prev is now", prev, "dp[i] is now", dp[i])
            print("min_index", min_index, "max_index", max_index)
            print(seen)
            if dp[i] != prev and prev not in seen:
                result.append(s[min_index:max_inde x +1])
                print("result", result)
                print("interval[i]", intervals[i])
                min_index = max_index+1
                max_index = intervals[i][1]
                seen.add(prev)
                prev = dp[i]
            else:
                min_index = min(min_index, intervals[i][0])
                max_index = max(max_index, intervals[i][1])
        print(min_index, max_index)
        return result



class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        left = defaultdict(lambda: float('inf'))
        right = defaultdict(lambda: float('-inf'))
        for i,c in enumerate(s):
            left[c] = min(left[c], i)
            right[c] = max(right[c], i)

        def extend(i):
            p = right[s[i]]
            j = i
            while j < p:
                c = s[j]
                if left[c] < i:
                    return -1
                p = max(p, right[c])
                j += 1
            return j

        last = -1
        ans = []
        for i, c in enumerate(s):
            if i != left[c]:
                continue
            j = extend(i)
            if j == -1:
                continue
            if i > last:
                ans += s[i:j+1],
            else:
                ans[-1] = s[i:j+1]
            last = j
        return ans





