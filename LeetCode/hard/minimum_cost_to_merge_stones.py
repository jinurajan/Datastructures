"""
Minimum Cost to Merge Stones

There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

 

Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.

Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        N = len(stones)
        dp = [[[10 ** 9] * (K + 1) for i in range(N + 1)] for j in range(N + 1)]

        for i in range(N + 1):
            dp[i][i][1] = 0  # the initial value

        for l in range(2, N + 1):  # length of [i,j], range from 2 to N
            for i in range(1, N + 2 - l):  # i moves forward, but keep j=i+l-1<N+1
                j = i + l - 1
                summ = sum(stones[i - 1:j])  # the temporary summation of stones[i-1:j], add this value to dp[i][j][k]
                for k in range(2, K + 1):  # compute k from 2 to K, then fill k=1
                    temp_res = 10 ** 9
                    for div in range(i, j):
                        temp_res = min(temp_res, dp[i][div][1] + dp[div + 1][j][k - 1])  # divide the [i:j] into 2 parts
                    dp[i][j][k] = temp_res
                dp[i][j][1] = summ + dp[i][j][k]  # finally compute dp[i][j][1]

        return dp[1][-1][1] if dp[1][-1][1] < 10 ** 9 else -1
