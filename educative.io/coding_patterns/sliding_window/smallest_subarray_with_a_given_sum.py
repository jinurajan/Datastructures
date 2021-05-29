"""
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
"""

def smallest_subarray_with_given_sum(s, arr):
    n = len(arr)
    left = 0
    right = 0
    sum_val = 0
    min_len = float("inf")
    while right < n:
        sum_val += arr[right]
        while sum_val >= s:
            min_len = min(min_len, right-left+1)
            sum_val -= arr[left]
            left += 1
        right += 1
    if min_len == float("inf"):
        return 0
    return min_len

print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


