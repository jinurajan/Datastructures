"""
Given an array of positive integers nums and a positive integer target, find the window size of the shortest contiguous subarray whose sum is greater than or equal to the target value. If no subarray is found, 0 is returned.
"""

def min_sub_array_len(target, nums):
    min_length = float("inf")
    n = len(nums)
    start, end = 0, 0
    window_sum = 0
    while end < n:
        window_sum += nums[end]
        while window_sum >= target:
            min_length = min(min_length, end-start+1)
            window_sum -= nums[start]
            start += 1
        end += 1
    return min_length if min_length != float("inf") else 0

def main():
    target = [7, 4, 11, 10, 5, 15]
    input_arr = [[2, 3, 1, 2, 4, 3],
                      [1, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 2, 3, 4], [1, 2, 1, 3],
                      [5, 4, 9, 8, 11, 3, 7, 12, 15, 44]]
    for i in range(len(input_arr)):
        window_size = min_sub_array_len(target[i], input_arr[i])
        print(i+1, ".\t min_sub_array_len(",
              target[i], ", ", (input_arr[i]), "): ", window_size, sep="")
        print("-"*100)


if __name__ == "__main__":
    main()