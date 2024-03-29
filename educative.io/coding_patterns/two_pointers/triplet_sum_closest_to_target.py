"""
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""
def triplet_sum_close_to_target(arr, target_sum):
  arr.sort()
  n = len(arr)
  min_diff = float("inf")
  for i in range(n-2):
    left = i+1
    right = n-1
    while left < right:
      triplet_diff = target_sum - (arr[i] + arr[left] + arr[right])
      if triplet_diff == 0:
        return target_sum - target_diff
      if abs(triplet_diff) < abs(min_diff) or (abs(triplet_diff) == abs(min_diff) and triplet_diff > min_diff):
        min_diff = triplet_diff
      if triplet_diff > 0:
        left += 1
      else:
        right -= 1
  return target_sum - min_diff
