"""
Maximize Score After N Operations

You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.


Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11


Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14


"""
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo_size = 1 << len(nums) # 2^n
        memo = [-1] * memo_size
        return self.backtrack(nums, 0, 0, memo)
    

    def backtrack(self, nums:List[int], mask:int, pairs_picked:int, memo:List[int]) -> int:
        if 2 * pairs_picked == len(nums):
            return 0
        if memo[mask] != -1:
            return memo[mask]
        max_score = 0
        for first_idx in range(len(nums)):
            for second_idx in range(first_idx+1, len(nums)):
                if (mask >> first_idx) & 1 == 1 or (mask >> second_idx) & 1 == 1:
                    continue
                new_mask = mask | (1 << first_idx) | (1 << second_idx)

                curr_score = (pairs_picked+1) * math.gcd(nums[first_idx], nums[second_idx])
                remaining_score= self.backtrack(nums, new_mask, pairs_picked+1, memo)

                max_score = max(max_score, curr_score+remaining_score)
        memo[mask] = max_score
        return max_score


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        max_states = 1 << len(nums) # 2^n
        final_mask = max_states-1

        dp = [0] * max_states
    
        for state in range(final_mask, -1, -1):
            if state == final_mask:
                dp[state] = 0
                continue
            numbers_taken = bin(state).count('1')
            pairs_formed = numbers_taken // 2

            if numbers_taken % 2:
                continue

            for first_idx in range(len(nums)):
                for second_idx in range(first_idx+1, len(nums)):
                    if (state >> first_idx & 1) == 1 or (state >> second_idx & 1) == 1:
                        continue
                    curr_score = (pairs_formed + 1) *(math.gcd(nums[first_idx], nums[second_idx]))
                    state_after_picking_curr_pair = state | (1 << first_idx) | (1 << second_idx)
                    remaining_score = dp[state_after_picking_curr_pair]
                    dp[state] = max(dp[state], curr_score + remaining_score)

        return dp[0]    
    
    
