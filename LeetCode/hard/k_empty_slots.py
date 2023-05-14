"""
You have n bulbs in a row numbered from 1 to n. Initially, all the bulbs are turned off. We turn on exactly one bulb every day until all bulbs are on after n days.

You are given an array bulbs of length n where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

Given an integer k, return the minimum day number such that there exists two turned on bulbs that have exactly k bulbs between them that are all turned off. If there isn't such day, return -1.

 

Example 1:

Input: bulbs = [1,3,2], k = 1
Output: 2
Explanation:
On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.
Example 2:

Input: bulbs = [1,2,3], k = 1
Output: -1
 

Constraints:

n == bulbs.length
1 <= n <= 2 * 104
1 <= bulbs[i] <= n
bulbs is a permutation of numbers from 1 to n.
0 <= k <= 2 * 104
"""
from typing import List

class Solution:

    def kEmptySlots(self, bulbs: List[int], k: int) -> int:

        def binary_search(intervals, pos):
            start, end = 0, len(intervals)- 1
            while start <=end:
                mid = (start+end) // 2
                if intervals[mid][0] <= pos and intervals[mid][1] >= pos:
                    return mid
                elif intervals[mid][0] > pos:
                    end = mid -1
                else:
                    start = mid + 1
            return -1

        bulb_pos = [0] * (len(bulbs)+1)
        for day, pos in enumerate(bulbs):
            bulb_pos[day+1] = pos

        intervals = [[1, len(bulbs)]]
        for day in range(1, len(bulbs)+1):
            pos = bulb_pos[day]
            i = binary_search(intervals, pos)
            if i == -1:
                continue
            start, end = intervals.pop(i)

            if day >= 2:
                if ((pos-start) == k and start != 1) or (end != len(bulbs) and (end-pos == k)):
                    return day
            if end - pos > k:
                intervals.insert(i, [pos+1, end])
            if pos - start >k:
                intervals.insert(i, [start, pos-1])
        return -1