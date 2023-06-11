"""
You are given n
 items whose weights and values are known, as well as a knapsack to carry these items. The knapsack cannot carry more than a certain maximum weight, known as its capacity.

You need to maximize the total value of the items in your knapsack, while ensuring that the sum of the weights of the selected items does not exceed the capacity of the knapsack.

If there is no combination of weights whose sum is within the capacity constraint, return 0
"""

from functools import lru_cache
def find_max_knapsack_profit(capacity, weights, values):

    # Replace this placeholder return statement with your code
    n = len(weights)
    def find_max_profit(index, capacity):
        if capacity < 0 or index == n:
            return 0
        if weights[index] <= capacity:
            # include
            return max(
                values[index] + find_max_profit(index+1, capacity-weights[index]),
                find_max_profit(index+1, capacity)
                )
        else:
            return find_max_profit(index+1, capacity)

    return find_max_profit(0, capacity)


def find_max_knapsack_profit(capacity, weights, values):

    # Replace this placeholder return statement with your code
    n = len(weights)
    @lru_cache(maxsize=None)
    def find_max_profit(index, capacity):
        if capacity < 0 or index == n:
            return 0
        if weights[index] <= capacity:
            # include
            return max(
                values[index] + find_max_profit(index+1, capacity-weights[index]),
                find_max_profit(index+1, capacity)
                )
        else:
            return find_max_profit(index+1, capacity)

    return find_max_profit(0, capacity)


def find_max_knapsack_profit(capacity, weights, values):
    # bottom up approach
    dp = [[0 for i in range(capacity+1)] for j in range(len(values))]
    
    # can you make 0 from any weights
    for c in range(capacity+1):
        if weights[0] <= c:
            dp[0][c] = values[0]
        
    for i in range(len(weights)):
        for c in range(1, capacity+1):
            p1, p2 = 0, 0
            if weights[i] <= c:
                p1 = values[i] + dp[i-1][c-weights[i]]
            p2 = dp[i-1][c]
            dp[i][c] = max(p1, p2)
    return dp[n-1][capacity]



def find_max_knapsack_profit_topdown(dp, values, weights, capacity, index):
    if index >= len(values) or capacity <= 0:
        return 0
    if dp[index][capacity] == -1:
        p1 = 0
        if weights[index] <= capacity:
            p1 = values[index] + find_max_knapsack_profit_topdown(dp, values, weights, capacity - weights[index], index + 1)

        p2 = find_max_knapsack_profit_topdown(dp, values, weights, capacity, index + 1)
        dp[index][capacity] =  max(p1, p2)
    return dp[index][capacity]

def find_max_knapsack_profit(capacity, weights, values):
    # top down approach
    n = len(values)
    dp = [[-1 for i in range(capacity+1)] for _ in range(n)]
    return find_max_knapsack_profit_topdown(dp, values, weights, capacity, 0)

