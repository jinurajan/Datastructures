"""
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. The only difference between the 0/1 Knapsack problem and this problem is that we are allowed to use an unlimited quantity of an item.

Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Melon }
Weights: { 1, 2, 3 }
Profits: { 15, 20, 50 }
Knapsack capacity: 5

Let’s try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5.

5 Apples (total weight 5) => 75 profit
1 Apple + 2 Oranges (total weight 5) => 55 profit
2 Apples + 1 Melon (total weight 5) => 80 profit
1 Orange + 1 Melon (total weight 5) => 70 profit

This shows that 2 apples + 1 melon is the best combination, as it gives us the maximum profit and the total weight does not exceed the capacity.

Problem Statement #
Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. We can assume an infinite supply of item quantities; therefore, each item can be selected multiple times.


"""

def solve_knapsack(profits, weights, capacity):
    """
    Time complexity = O(2 raised to (N+C))
    Space Complexity = O(N+C) for recursive stack
    """
    return solve_knapsack_recursive(profits, weights, capacity, 0)

def solve_knapsack_recursive(profits, weights, capacity, index):
    if capacity <= 0 or index >= len(weights):
        return 0
    p1, p2 = 0, 0
    if weights[index] <= capacity:
        p1 = profits[index] + solve_knapsack_recursive(profits, weights,capacity-weights[index], index)

    p2 = solve_knapsack_recursive(profits, weights, capacity, index+1)
    return max(p1, p2)


def solve_knapsack_top_down(profits, weights, capacity):
    """
    Time complexity = O(N * C)
    Space complexity = O(N *C)
    """

    dp = [[-1 for i in range(capacity+1)] for j in range(len(weights))]
    n = len(weights)
    def search(index, capacity):
        if capacity <= 0 or index >= n:
            return 0
        if dp[index][capacity] == -1:
            p1, p2 = 0, 0
            if weights[index] <= capacity:
                p1 = profits[index] + solve_knapsack_recursive(profits, weights, capacity - weights[index], index)
            p2 = solve_knapsack_recursive(profits, weights, capacity, index + 1)
            dp[index][capacity] = max(p1, p2)

        return dp[index][capacity]
    return search(0, capacity)


def solve_knapsack_bottom_up(profits, weights, capacity):
    """
    Time complexity = O(N * C)
    Space complexity = O(N *C)
    """
    if not weights or not capacity:
        return 0
    n = len(weights)
    dp = [[0 for i in range(capacity+1)] for j in range(n)]
    for i in range(n):
        for j in range(1, capacity+1):
            p1, p2 = 0, 0
            if j >= weights[i]:
                p1 = profits[i] + dp[i][j-weights[i]]
            p2 = dp[i-1][j]
            dp[i][j] = max(p1, p2)
    return dp[n-1][capacity]





print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))

print(solve_knapsack_top_down([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(solve_knapsack_top_down([15, 50, 60, 90], [1, 3, 4, 5], 6))

print(solve_knapsack_bottom_up([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(solve_knapsack_bottom_up([15, 50, 60, 90], [1, 3, 4, 5], 6))