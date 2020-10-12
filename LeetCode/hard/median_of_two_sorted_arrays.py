"""
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        def median(arr):
            import pdb; pdb.set_trace()
            n = len(arr)
            if n % 2 == 1:
                return arr[n // 2]
            else:
                return (arr[n // 2] + arr[ (n // 2)-1]) / 2
        if not nums1:
            return median(nums2)
        if not nums2:
            return median(nums1)


        def merge(arr1, arr2):
            result = []
            n1 = len(arr1)
            n2 = len(arr2)
            i, j = 0, 0
            while i < n1 and j < n2:
                if arr1[i] < arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1
            if j < n2:
                # arr1 is over
                for k in range(j, n2):
                    result.append(nums2[k])
            if i < n1:
                for k in range(i, n1):
                    result.append(nums1[k])
            return result

        result = merge(nums1, nums2)
        return median(result)



nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))
nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))


