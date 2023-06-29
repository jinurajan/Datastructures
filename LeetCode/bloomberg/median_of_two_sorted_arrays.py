"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



1. one min heap and one max heap
max_heap to store the first half of the sorted elements
min_heap to store the second half of the sorted elements
min_heap will store the extra elements if total numbers are odd

"""
from typing import List
from heapq import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        p1 , p2 = 0, 0

        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans
        
        if (m+n) % 2 == 0:
            for _ in range((m+n)//2 -1):
                _ = get_min()
            return (get_min() + get_min()) / 2
        else:
            for _ in range((m+n)//2):
                _ = get_min()
            return get_min()


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        min_heap = []
        max_heap = []

        def insert_into_heaps(nums):
            for num in nums:
                heappush(min_heap, num)
                heappush(max_heap, -heappop(min_heap))
                if len(max_heap) > len(min_heap):
                    heappush(min_heap, -heappop(max_heap))
        
        insert_into_heaps(nums1)
        insert_into_heaps(nums2)
        if len(min_heap) == len(max_heap):
            return heappop(min_heap)/2.0 + -heappop(max_heap) / 2.0
        else:
            return heappop(min_heap) / 1.0



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        p1 , p2 = 0, 0

        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans
        
        if (m+n) % 2 == 0:
            for _ in range((m+n)//2 -1):
                _ = get_min()
            return (get_min() + get_min()) / 2
        else:
            for _ in range((m+n)//2):
                _ = get_min()
            return get_min()






from heapq import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        na, nb = len(nums1), len(nums2)
        n = na + nb

        def solve(k, a_start, a_end, b_start, b_end):
            if a_start > a_end:
                return nums2[k-a_start]
            if b_start > b_end:
                return nums1[k-b_start]
            
            a_index, b_index = (a_start + a_end) // 2, (b_start+b_end) // 2

            a_value , b_value = nums1[a_index], nums2[b_index]
            # If k is in the right half of A + B, remove the larger right half.
            if a_index + b_index < k :
                if a_value > b_value:
                    return solve(k, a_start, a_end, b_index+1, b_end)
                else:
                    return solve(k, a_index+1, a_end, b_start, b_end)
            # Otherwise, remove the smaller left half
            else:
                if a_value > b_value:
                    return solve(k, a_start, a_index-1, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_start, b_index-1)
        
        if n % 2:
            return solve(n//2, 0, na-1, 0, nb-1)
        else:
            return (solve(n//2-1, 0, na-1, 0, nb-1) + solve(n//2, 0, na-1, 0, nb-1)) / 2 



    

nums1 = [5,102, 104]
nums2 = [100, 101, 103]
Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2)
