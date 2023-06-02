"""
Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) of size w.

Note: If the window size is greater than the array size, we consider the entire array as a single window.
"""

from collections import deque
def find_max_sliding_window(nums, window_size):
    window_size = min(len(nums), window_size)
    result = []
    window = deque()
    if not nums:
        return result
    for i in range(window_size):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)
    result.append(nums[window[0]])
    count = 0
    for i in range(window_size, len(nums)):
        while window and nums[i] >= nums[window[-1]]:
           window.pop()
        if window and window[0] <= i - window_size:
            window.popleft()
        window.append(i)
        result.append(nums[window[0]])
    return result

def main():
    target_list = [3, 3, 3, 3, 2, 4, 3, 2, 3, 18, 2]
    nums_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                 [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                 [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                 [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30],
                 [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
                 [4, 5, 6, 1, 2, 3],
                 [9, 5, 3, 1, 6, 3],
                 [2, 4, 6, 8, 10, 12, 14, 16],
                 [-1, -1, -2, -4, -6, -7],
                 [4, 4, 4, 4, 4, 4],
                 [7,2,4]]

    for i in range(len(nums_list)):
        print(i + 1, ".\tOriginal array:\t", nums_list[i], sep="")
        print("\tWindow size:\t", target_list[i])
        print("\n\tMax:\t\t",
              find_max_sliding_window(nums_list[i], target_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()


