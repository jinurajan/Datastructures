"""
Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.



Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]


Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter()
        suffix_array = []
        no_set = set(arr2)
        for i, num in enumerate(arr1):
            if num in no_set:
                counter[num] += 1
            else:
                suffix_array.append(num)
        suffix_array.sort()
        prefix_array = []
        for num in arr2:
            for i in range(counter[num]):
                prefix_array.append(num)
        return prefix_array + suffix_array
