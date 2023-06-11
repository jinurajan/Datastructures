"""
Given a non-empty array of positive integers, determine if the array can be divided into two subsets so that the sum of both subsets is equal.

"""

def can_partition_array(nums):
    s = sum(nums)
    if s % 2 == 1:
        # odd number sum
        return False
    return can_partition_array_recursive(nums, 0, s//2)

def can_partition_array_recursive(nums, index, sum):
    if sum == 0:
        return True
    if sum < 0 or index >= len(nums):
        return False
    if nums[index] <= sum:
        if can_partition_array_recursive(nums, index+1, sum-nums[index]):
            return True
    return can_partition_array_recursive(nums, index+1, sum)
    
    

from functools import lru_cache

def can_partition_array(nums):
    s = sum(nums)
    if s % 2 == 1:
        # odd number sum
        return False
    
    @lru_cache(maxsize=None)
    def can_partition_array_recursive(index, sum):
        if sum == 0:
            return True
        if sum < 0 or index >= len(nums):
            return False
        if nums[index] <= sum:
            if can_partition_array_recursive(index+1, sum-nums[index]):
                return True
        return can_partition_array_recursive(index+1, sum)

    return can_partition_array_recursive(0, s//2)
    
    

def can_partition_array_topdown(nums):
    s = sum(nums)
    if s % 2 == 1:
        # odd number sum
        return False
    dp = [[-1 for i in range((s//2)+1)] for j in range(len(nums))]
    
    def can_partition_array_recursive(dp, index, sum):
        if sum == 0:
            return True
        if sum < 0 or index >= len(nums):
            return False
        if dp[index][sum] == -1:
            if nums[index] <= sum:
                dp[index][sum] = can_partition_array_recursive(dp, index+1, sum-nums[index])
            else:
                dp[index][sum] = can_partition_array_recursive(dp, index+1, sum)
        return dp[index][sum]

    return can_partition_array_recursive(dp, 0, s//2)


def can_partition_bottomup(nums):
    s = sum(nums)
    if s % 2 == 1:
        return False
    n = len(nums)
    s = int(s/2)
    dp = [[False for _ in range(s+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = True

    for j in range(1, s+1):
        dp[0][j] = nums[0] == j

    for i in range(1, n):
        for j in range(1, s+1):
            if dp[i-1][j]:
                dp[i][j] = dp[i-1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i-1][j-nums[i]]
    return dp[n-1][s]