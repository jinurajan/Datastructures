"""
Check Array Formation Through Concatenation

You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
Return true if it is possible to form the array arr from pieces. Otherwise, return false

Input: arr = [85], pieces = [[85]]
Output: true

Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]

Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].

Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]

Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false

Constraints:

1 <= pieces.length <= arr.length <= 100
sum(pieces[i].length) == arr.length
1 <= pieces[i].length <= arr.length
1 <= arr[i], pieces[i][j] <= 100
The integers in arr are distinct.
The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
"""
from typing import List
from collections import deque

class Solution1:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        start_index = 0
        index_set = list(range(len(pieces)))
        while start_index < len(arr):
            found = False
            for i in index_set:
                if pieces[i][0] == arr[start_index]:
                    # found the piece check for all other elements
                    index_set.remove(i)
                    found = True
                    window_index = len(pieces[i])
                    if arr[start_index:start_index+window_index] != pieces[i]:
                        return False
                    start_index += window_index
            if not found:
                return  False
        return True

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        for piece in pieces:
            try:
                index = arr.index(piece[0])
                if arr[index: index+len(piece)] != piece:
                    return  False
            except:
                return  False
        return True

arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]
print(Solution().canFormArray(arr, pieces))

arr = [49,18,16]
pieces = [[16,18,49]]
print(Solution().canFormArray(arr, pieces))

arr = [85]
pieces = [[85]]
print(Solution().canFormArray(arr, pieces))

arr = [15,88]
pieces = [[88],[15]]
print(Solution().canFormArray(arr, pieces))


arr = [1,3,5,7]
pieces = [[2,4,6,8]]
print(Solution().canFormArray(arr, pieces))

arr = [2,82,79,95,28]
pieces = [[2],[82],[28],[79,95]]
print(Solution().canFormArray(arr, pieces))

