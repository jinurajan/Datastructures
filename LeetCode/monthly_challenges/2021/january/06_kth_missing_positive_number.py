"""
Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.


Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.


Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.


Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length

"""
from typing import List

class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if not arr:
            return k
        total_sum = int(len(arr) * (len(arr) + 1) / 2 )
        if sum(arr) == total_sum:
            return arr[-1] + k
        else:
            val = 0
            i = 0
            e = 1
            counter = 0
            while i < len(arr):
                if arr[i] == e:
                    i += 1
                    e += 1
                else:
                    val = e
                    e += 1
                    counter += 1
                if counter == k:
                    return val
            if counter < k:
                if arr[-1] > val:
                    return arr[-1] + (k - counter)
                return val + (k - counter)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        i = 1
        curr = 0
        res = 0
        while curr < k:
            if i not in arr_set:
                curr += 1
                res = i
            i += 1
        return res



arr = [2,3,4,7,11]
k = 5
print(Solution().findKthPositive(arr, k))

arr = [1,2,3,4]
k = 2
print(Solution().findKthPositive(arr, k))

arr = []
k = 4
print(Solution().findKthPositive(arr, k))

arr = [2,3,4,7,11]
k = 9
print(Solution().findKthPositive(arr, k))


arr = [5,6,7,8,9]
k = 9
print(Solution().findKthPositive(arr, k))





