"""
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].


"""


def remove_duplicates(arr):
  non_dup = 1
  n = len(arr)
  for i in range(n):
    if arr[non_dup-1] != arr[i]:
      arr[i], arr[non_dup] = arr[non_dup], arr[i]
      non_dup += 1

  return non_dup

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))
