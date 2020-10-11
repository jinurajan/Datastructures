"""
Duplicate Zeros

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""
from typing import List

class Solution1:
    def duplicateZeros(self, arr: List[int]) -> None:

        i = 0
        while i < len(arr) - 1:
            if arr[i] != 0:
                i += 1
            else:
                arr[i+2:], arr[i+1] = arr[i+1:len(arr)-1], 0
                i += 2

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        offset = 0
        right_index = len(arr) - 1

        # Find the number of zeros to be duplicated
        for index in range(right_index + 1):
            if index > right_index - offset:
                break
                
            if arr[index] == 0:
                if index == right_index - offset:
                    arr[right_index] = 0
                    right_index -= 1
                    break
                offset += 1

        for i in range(right_index - offset, -1, -1):
            if arr[i] == 0:
                arr[i + offset] = 0
                offset -= 1
                arr[i + offset] = 0
            else:
                arr[i + offset] = arr[i]

import pdb; pdb.set_trace()
arr = [1,0,2,3,0,4,5,0]
print(Solution().duplicateZeros(arr))
print(arr)
arr = [8,5,0,9,0,3,4,7]
print(Solution().duplicateZeros(arr))
print(arr)
arr = [8,4,5,0,0,0,0,7]
print(Solution().duplicateZeros(arr))
print(arr)


