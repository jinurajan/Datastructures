"""
Find K Closest Elements

Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10^4
Absolute value of elements in the array and x will not exceed 104

"""
from typing import List
from bisect import bisect_left
from math import ceil, floor


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # base cases k is greater than len(arr)
        n = len(arr)
        if k >= n:
            return arr
        
        def binary_search(nums, l, r, x):
            if l < r:
                mid = (l + r)// 2
                if nums[mid] == x:
                    return mid
                if nums[mid] < x:
                    return binary_search(nums, mid+1, r, x)
                return binary_search(nums, l, mid-1, x)
            return l

        
        if x <=arr[0]:
            return arr[:k]
        elif x >= arr[-1]: 
            return arr[-k:]
        else:
            index = binary_search(arr, 0, len(arr)-1, x)
            l, r = max(0, index-k-1), min(n-1, index+k-1)
            while r-l > k-1:
                if l < 0 or x-arr[l] <= arr[r]-x:
                    r -= 1
                elif r > n-1 or x-arr[l] > arr[r]-x:
                    l += 1
            return arr[l:r+1]


class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # base cases k is greater than len(arr)
        n = len(arr)
        if k >= n:
            return arr
        
        def binary_search(arr, l, r, x):
            l, r = 0, len(arr)-1
            while l < r:
                mid = (l + r) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] > x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
       
        
        if x <=arr[0]:
            return arr[:k]
        elif x >= arr[-1]: 
            return arr[-k:]
        else:
            index = binary_search(arr, 0, len(arr)-1, x)
            l, r = max(0, index-k-1), min(n-1, index+k-1)
            while r-l > k-1:
                if l < 0 or x-arr[l] <= arr[r]-x:
                    r -= 1
                elif r > n-1 or x-arr[l] > arr[r]-x:
                    l += 1
            return arr[l:r+1]


class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # base cases k is greater than len(arr)
        n = len(arr)
        if k >= n:
            return arr
        if x <=arr[0]:
            return arr[:k]
        elif x >= arr[-1]: 
            return arr[-k:]
        else:
            index = bisect_left(arr, x)
            l, r = max(0, index-k-1), min(n-1, index+k-1)
            while r-l > k-1:
                if l < 0 or x-arr[l] <= arr[r]-x:
                    r -= 1
                elif r > n-1 or x-arr[l] > arr[r]-x:
                    l += 1
            return arr[l:r+1]


            


print(Solution().findClosestElements([1,2,3,4,5], k = 4, x = 3))
print(Solution().findClosestElements([1,2,3,4,5], k = 2, x = 3))
print(Solution().findClosestElements([1,2,3,4,5], k = 3, x = 3))
print(Solution().findClosestElements([1,2,3,4,5], k = 5, x = 3))

print(Solution().findClosestElements([1,2,3,4,5], k = 4, x = -1))
print(Solution().findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4))

