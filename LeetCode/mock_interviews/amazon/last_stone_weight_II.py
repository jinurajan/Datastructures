"""
Last Stone Weight II

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.



Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

Input: stones = [31,26,33,21,40]
Output: 5
Example 3:

Input: stones = [1,2]
Output: 1


Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 100

"""
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        # S1 + S2 = S
        # S1 - S2 = d
        # -------------
        # 2*S1 = S + d
        # d = S - 2*S1

        # minimizing d is maximizing S1

        S = sum(stones)

        @cache
        def dp(N, k):
            if k == 0:
                return True
            if N == 0:
                return False

            if stones[N - 1] <= k:
                return dp(N - 1, k - stones[N - 1]) or dp(N - 1, k)
            return dp(N - 1, k)

        N = len(stones)

        if N == 1:
            return stones[0]

        for s1 in range(S // 2, 0, -1):
            if dp(N, s1):
                return S - 2 * s1

        return 0




class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        capacity = sum(stones) // 2
        n = len(stones)

        table = {}

        def knapsack(capacity, n):
            if (capacity, n) in table: return table[(capacity, n)]
            if capacity == 0 or n == 0:
                return 0
            if capacity - stones[n - 1] >= 0:
                table[(capacity, n)] = max(stones[n - 1] + knapsack(capacity - stones[n - 1], n - 1),
                                           knapsack(capacity, n - 1))
                return table[(capacity, n)]
            else:
                table[(capacity, n)] = knapsack(capacity, n - 1)
                return table[(capacity, n)]

        first = knapsack(capacity, n)
        second = sum(stones) - first
        return abs(first - second)
