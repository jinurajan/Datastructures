"""
Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.

Example 1:

Input = {2,1,1,1,4}
Output = 3
Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4
Example 2:

Input = {1,1,3,6,9,3,0,1,3}
Output = 4
Explanation: Starting from index '0', we can reach the last index through: 0->1->2->3->8
"""
import math

def count_min_jumps(jumps):
  return count_min_jumps_recursive(jumps, 0)


def count_min_jumps_recursive(jumps, index):
    n = len(jumps)
    if index  == n - 1:
         # reached end of array
        return 0
    if jumps[index] == 0:
        # not possible to jump
        return math.inf
    total_jumps  = math.inf
    start, end = index+1, index + jumps[index]
    while start < n and start <= end:
        min_jumps = count_min_jumps_recursive(jumps, start)
        start += 1
        if min_jumps != math.inf:
            total_jumps = min(total_jumps, min_jumps+1)
    return total_jumps


def count_min_jumps_top_down(jumps):
    n = len(jumps)
    dp = [0 for i in range(n)]

    def count_min_jumps(index):
        if index == n - 1:
            return 0
        if jumps[index] == 0:
            return math.inf
        if dp[index] != 0:
            return dp[index]
        total_jumps = math.inf
        start, end = index + 1, index + jumps[index]
        while start < n and start <= end:
            min_jumps = count_min_jumps(start)
            start += 1
            if min_jumps != math.inf:
                total_jumps = min(total_jumps, min_jumps + 1)
        return total_jumps
    return  count_min_jumps(0)



def count_min_jumps_bottom_up(jumps):
    n = len(jumps)
    dp = [math.inf for i in range(n)]
    dp[0] = 0
    for start in range(n-1):
        end = start + 1
        while end <= start + jumps[start] and end < n:
            dp[end] = min(dp[end], dp[start]+1)
            end += 1
    return dp[-1]


print(count_min_jumps([2, 1, 1, 1, 4]))
print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))

print(count_min_jumps_top_down([2, 1, 1, 1, 4]))
print(count_min_jumps_top_down([1, 1, 3, 6, 9, 3, 0, 1, 3]))

print(count_min_jumps_bottom_up([2, 1, 1, 1, 4]))
print(count_min_jumps_bottom_up([1, 1, 3, 6, 9, 3, 0, 1, 3]))



