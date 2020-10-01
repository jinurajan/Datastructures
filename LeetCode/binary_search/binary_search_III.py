"""
Template #3 is another unique form of Binary Search. 
It is used to search for an element or condition which 
requires accessing the current index and its immediate 
left and right neighbor's index in the array.

Key Attributes:

An alternative way to implement Binary Search
Search Condition needs to access element's immediate left and right neighbors
Use element's neighbors to determine if condition is met and decide whether to go left or right
Gurantees Search Space is at least 3 in size at each step
Post-processing required. Loop/Recursion ends when you have 2 elements left. 
Need to assess if the remaining elements meet the condition. 

Distinguishing Syntax:

Initial Condition: left = 0, right = length-1
Termination: left + 1 == right
Searching Left: right = mid
Searching Right: left = mid
"""

def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1


def binarySearch1(nums, target):
    if len(nums) == 0:
        return -1

    def bin_search(nums, l, r, target):
        if l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bin_search(nums, mid, r, target)
            else:
                return bin_search(nums, l, mid, target)
        return l

    l = bin_search(nums, 0, len(nums)-1, target)
    if nums[l] == target: return l
    if nums[l+1] == target: return l + 1
    if nums[l+2] == target: return l + 2
    return -1


print(binarySearch([4, 5,6, 8, 10, 11], 11))
print(binarySearch([4, 5,6, 8, 10, 11], 4))
print(binarySearch([4, 5,6, 8, 10, 11], 8))
print(binarySearch([4, 5,6, 8, 10, 11], 9))
print("***********")

print(binarySearch1([4, 5,6, 8, 10, 11], 11))
print(binarySearch1([4, 5,6, 8, 10, 11], 4))
print(binarySearch1([4, 5,6, 8, 10, 11], 8))
print(binarySearch1([4, 5,6, 8, 10, 11], 9))





