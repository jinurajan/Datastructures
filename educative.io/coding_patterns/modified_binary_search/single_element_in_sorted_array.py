"""
In this problem, you’re given an array of sorted integers in which all of the integers, except one, appears twice. Your task is to find the single integer that appears only once.

The solution should have a time complexity of O(logn) or better and a space complexity of O(1)
"""

def single_non_duplicate(nums): 

  # Write your code here to find the single element in a sorted array.
  
  # You may use the code template provided in the binary_search.py file.
    low = 0
    high = len(nums)-1
    while low < high:
        mid = (low+high) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid+1]:
            low = mid+2
        else:
            high = mid
    return nums[low]


## Driver Code

def main():

    nums = [[1, 2, 2, 3, 3, 4, 4], [1, 1, 2, 2, 3, 4, 4, 5, 5], [1, 1, 2, 3, 3], [1, 1, 2], [0, 2, 2, 3, 3, 4, 4, 5, 5]]

    for i in range(len(nums)):
        print(str(i + 1) + ".\tThe Array = ", nums[i] , sep = "")
        print("\tSingle Element Found: ", single_non_duplicate(nums[i]), sep = "")
        print("-" * 100)

if __name__ == '__main__':
    main()