"""
Duplicate Zeros

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9

"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return arr
        zeros = arr.count(0)
        cur_idx = len(arr) - 1
        while zeros > 0:
            if cur_idx + zeros < len(arr):
                arr[cur_idx+zeros] = arr[cur_idx]
            if arr[cur_idx] == 0:
                zeros -= 1
                if cur_idx + zeros < len(arr):
                    arr[cur_idx + zeros] = arr[cur_idx]
            cur_idx -= 1
        return arr


arr = [1,0,2,3,0,4,5,0]
print(Solution().duplicateZeros(arr))

arr = [1,2,3]
print(Solution().duplicateZeros(arr))

arr = [1]
print(Solution().duplicateZeros(arr))

arr = [1, 0]
print(Solution().duplicateZeros(arr))

arr = [1, 0, 1]
print(Solution().duplicateZeros(arr))

arr = [0,0,0]
print(Solution().duplicateZeros(arr))

arr = [9,0,9,0,6,0,0,0,1,1,6,5,4,4,8,3,0,0,0,1,5,3,0,0,7,2,1,0,2,0,9,1,0,2,0,0,0,0,0,0,0,6,0,0,7,9,0,8,7,0,9,7,1,0,2,0,0,0,0,9,0,0,0,0]
print(Solution().duplicateZeros(arr) == [9,0,0,9,0,0,6,0,0,0,0,0,0,1,1,6,5,4,4,8,3,0,0,0,0,0,0,1,5,3,0,0,0,0,7,2,1,0,0,2,0,0,9,1,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0])

arr = [1, 0, 2, 3, 0, 0, 5, 4]
print(Solution().duplicateZeros(arr))
