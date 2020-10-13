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


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Take
        Start with mid which is n1 + n2 + 1 // 2
        check if the left side length is equal to 
        """
        def median(arr):
            n = len(arr)
            if n % 2 == 1:
                return arr[n // 2]
            else:
                return (arr[n // 2] + arr[ (n // 2)-1]) / 2
        if not nums1:
            return median(nums2)
        if not nums2:
            return median(nums1)

        n1 = len(nums1)
        n2 = len(nums2)
        min_val = float("-inf")
        max_val = float("inf")

        if n2 > n1:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        import pdb; pdb.set_trace()
        start, end = 0, n1
        half_len = (n1 + n2 + 1 ) // 2
        while start <= end:
            partition_x = (start + end) // 2
            partition_y = half_len - partition_x
            max_left_x = nums1[partition_x-1] if partition_x != 0 else min_val
            min_right_x = nums1[partition_x] if partition_x != n1 else max_val

            max_left_y = nums2[partition_y-1] if partition_y != 0 else min_val
            min_right_y = nums2[partition_y] if partition_y != n2 else max_val

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # found the right partition
                if (n1 + n2) % 2 == 0:
                    # evenlength
                    return (max(max_left_x,max_left_y) + min(min_right_y, min_right_x)) / 2
                else:
                    return max(max_left_x,max_left_y)
            elif max_left_x > min_right_y:
                end = partition_x - 1
            else:
                start = partition_x + 1


            






nums1 = [1, 2]
nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))
nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))

nums1 = [4,5,6,7,8,9]
nums2 =[1, 2, 3 ]
"""
# 1, 2, 3,4 ,5, 6,7,8,9
start,end = 
# x [4,5,6]  [7,8,9]
# y [1, 2]   [3]
max_left_x 6
min_left_y 7

max_left_y 2
min_left_y 3


start = 3

loop 2

partionx = 

"""

print(Solution().findMedianSortedArrays(nums1, nums2))



