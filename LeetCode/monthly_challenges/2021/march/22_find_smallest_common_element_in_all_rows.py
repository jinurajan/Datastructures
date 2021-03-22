"""
Find Smallest Common Element in All Rows


Given a matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.



Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in strictly increasing order.


"""
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        def binary_search(array, k):
            l = 0
            r = len(array) - 1
            while l <= r:
                mid = (l + r) // 2
                if array[mid] == k:
                    return mid
                elif array[mid] > k:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        for n in mat[0]:
            is_common = True
            for rest in mat[1:]:
                if binary_search(rest, n) == -1:
                    is_common = False
                    break
            if is_common:
                return n
        return -1


from collections import Counter


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counter = Counter()
        mat_len = len(mat)
        for array in mat:
            for n in array:
                counter[n] = counter[n] + 1
        values = sorted([k for k, val in counter.items() if val == mat_len])
        if not values:
            return -1
        return values[0]




