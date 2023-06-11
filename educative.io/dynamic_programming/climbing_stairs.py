"""
You are climbing a staircase. It takes n steps to reach the top. Each time, you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climb_stairs(nums):
    dp = [0 for i in range(nums+1)]
    dp[1] = 1
    dp[2] = 2

    for i in range(3, nums+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[nums]


from functools import lru_cache

def climb_stairs(nums):
    # top down
    
    @lru_cache(maxsize=None)
    def climb_stairs_recursive(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        return climb_stairs_recursive(n-1) + climb_stairs_recursive(n-2)
    
    return climb_stairs_recursive(nums)
