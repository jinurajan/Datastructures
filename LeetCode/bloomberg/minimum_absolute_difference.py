"""
Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr


Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
"""

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        result = []
        for i in range(1, len(arr)):
            curr_pair_diff = arr[i] - arr[i-1]
            if min_diff == curr_pair_diff:
                result.append([arr[i-1], arr[i]])
            elif curr_pair_diff < min_diff:
                result = [[arr[i-1], arr[i]]]
                min_diff = curr_pair_diff

        return result

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float("inf")
        n1 = arr[0]
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - n1)
            n1 = arr[i]
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1], arr[i]])
        
        return result


                    