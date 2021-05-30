"""
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’ The goal is to get the maximum profit out of the knapsack items. Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:

Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination as it gives us the maximum profit, and the total weight does not exceed the capacity.

"""


def solve_knapsack(profits, weights, capacity):
    return solve_knapsack_recursive(profits, weights, capacity, 0)


def solve_knapsack_recursive(profits, weights, capacity, index):
    if index >= len(profits) or capacity <= 0:
        return 0

    p1 = 0
    if weights[index] <= capacity:
        p1 = profits[index] + solve_knapsack_recursive(profits, weights, capacity - weights[index], index + 1)

    p2 = solve_knapsack_recursive(profits, weights, capacity, index + 1)
    return max(p1, p2)


def solve_knapsack_topdown(profits, weights, capacity):
    n = len(profits)
    dp = [[-1 for i in range(capacity+1)] for _ in range(n)]
    return solve_knapsack_recursive_topdown(dp, profits, weights, capacity, 0)

def solve_knapsack_recursive_topdown(dp, profits, weights, capacity, index):
    if index >= len(profits) or capacity <= 0:
        return 0
    if dp[index][capacity] == -1:
        p1 = 0
        if weights[index] <= capacity:
            p1 = profits[index] + solve_knapsack_recursive_topdown(dp, profits, weights, capacity - weights[index], index + 1)

        p2 = solve_knapsack_recursive_topdown(dp, profits, weights, capacity, index + 1)
        dp[index][capacity] =  max(p1, p2)
    return dp[index][capacity]



def solve_knapsack_bottomup(profits, weights, capacity):
    n = len(profits)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n)]
    for c in range(capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, n):
        for c in range(1, capacity+1):
            p1, p2 = 0, 0
            if weights[i] <= c:
                p1 = profits[i] + dp[i-1][c-weights[i]]
            p2 = dp[i-1][c]
            dp[i][c] = max(p1, p2)
    return dp[n-1][capacity]


def solve_knapsack_bottomup_space_optimized(profits, weights, capacity):
    n = len(profits)
    dp = [[0 for _ in range(capacity+1)] for _ in range(2)]
    for c in range(capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, n):
        for c in range(1, capacity+1):
            p1, p2 = 0, 0
            if weights[i] <= c:
                p1 = profits[i] + dp[(i-1)%2][c-weights[i]]
            p2 = dp[(i-1)%2][c]
            dp[i%2][c] = max(p1, p2)
    return dp[(n-1)%2][capacity]



def solve_knapsack_bottomup_optimized(profits, weights, capacity):
    n = len(profits)
    dp = [0 for _ in range(capacity + 1)]
    for c in range(capacity+1):
        if weights[0] <= c:
            dp[c] = profits[0]
    for i in range(1, n):
        for c in range(capacity, -1, -1):
            p1, p2 = 0, 0
            if weights[i] <= c:
                p1 = profits[i] + dp[c-weights[i]]
            p2 = dp[c]
            dp[c] = max(p1, p2)
    return dp[-1]




print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
print("")
print(solve_knapsack_topdown([1, 6, 10, 16], [1, 2, 3, 5], 5))
print(solve_knapsack_topdown([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(solve_knapsack_topdown([1, 6, 10, 16], [1, 2, 3, 5], 7))
print("")

print(solve_knapsack_bottomup([1, 6, 10, 16], [1, 2, 3, 5], 5))
print(solve_knapsack_bottomup([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(solve_knapsack_bottomup([1, 6, 10, 16], [1, 2, 3, 5], 7))
print("")

print(solve_knapsack_bottomup_space_optimized([1, 6, 10, 16], [1, 2, 3, 5], 5))
print(solve_knapsack_bottomup_space_optimized([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(solve_knapsack_bottomup_space_optimized([1, 6, 10, 16], [1, 2, 3, 5], 7))
print("")

print(solve_knapsack_bottomup_optimized([1, 6, 10, 16], [1, 2, 3, 5], 5))
print(solve_knapsack_bottomup_optimized([1, 6, 10, 16], [1, 2, 3, 5], 6))
print(solve_knapsack_bottomup_optimized([1, 6, 10, 16], [1, 2, 3, 5], 7))


