"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""

def max_sub_array_of_size_k(k, arr):
    n = len(arr)
    left = 0
    right = 0
    s = 0
    max_sum_len = 0
    while right < n:
        s += arr[right]
        if right - left + 1 == k:
            max_sum_len = max(max_sum_len, s)
            s -= arr[left]
            left += 1
        right += 1
    return max_sum_len


print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))