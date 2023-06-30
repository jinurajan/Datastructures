"""
Peak Index in a Mountain Array

An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Input: arr = [0,1,0]
Output: 1

Input: arr = [0,2,1,0]
Output: 1


Input: arr = [0,10,5,2]
Output: 1
"""
from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        while arr[i] < arr[i+1]:
            i += 1
        return i


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)

        while l < r:
            mid = (l+r) // 2
            if arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l
