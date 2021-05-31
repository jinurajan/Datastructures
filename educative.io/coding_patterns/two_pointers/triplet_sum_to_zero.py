"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

"""


def search_triplets(arr):
    triplets = []
    arr.sort()
    n = len(arr)

    def two_sum(target, left, triplets):
        right = len(arr) - 1
        while left < right:
            curr = arr[left] + arr[right]
            if curr == target:
                triplets.append([-target, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while right >= 0 and arr[right] == arr[right + 1]:
                    right -= 1
            elif target > curr:
                left += 1  # we need a pair with a bigger sum
            else:
                right -= 1

    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        two_sum(-arr[i], i + 1, triplets)

    return triplets

