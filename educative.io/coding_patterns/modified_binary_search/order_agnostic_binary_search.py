"""
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Example 1:

Input: [4, 6, 10], key = 10
Output: 2
Example 2:

Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4
Example 3:

Input: [10, 6, 4], key = 10
Output: 0
Example 4:

Input: [10, 6, 4], key = 4
Output: 2
"""


def binary_search(arr, key):
    n = len(arr)
    left = 0
    right = n - 1
    is_asc = arr[left] < arr[right]

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        if is_asc:
            if key > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if key > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1



def binary_search(arr, key):
    n = len(arr)
    left = 0
    right = n - 1
    is_asc = arr[left] < arr[right]

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        if is_asc:
            if key > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if key > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
