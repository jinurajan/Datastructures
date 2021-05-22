"""

There are n items. its weights and profit is given and maximum capacity is also given. find the maximum profit you can make with this

1. we either include an object or do not include
2. since its bi decisional problem complexity is 2 raised to n
3. we can eliminate it by using dynamic programming / memoization

"""

# 1. how do we solve this in brute force. we try out all combinations and select the one with maximum profit



def knapsack(weights, profits, capacity):
    # Time complexity = O(2 raised to N - 1) where N is the number of items
    # space complexity - O(N) for recursive stack calls

    return knapsack_recursive(weights, profits, capacity, 0)


def knapsack_recursive(weights, profits, capacity, index):
    if capacity <= 0 or index >= len(weights):
        return 0
    p1 = 0
    if weights[index] <= capacity:
        p1 = profits[index] + knapsack_recursive(weights, profits, capacity-weights[index], index+1)
    p2 = knapsack_recursive(weights, profits, capacity, index+1)
    return max(p1, p2)



# topdown dynamic programming with memoization
def knapsack_using_dp_top_down(weights, profits, capacity):

    # time complexity = O(N * C)
    # space O(N*C) for array O(N) for recursion so total O(N*C+N)
    dp = [[-1 for i in range(capacity+1)] for j in range(len(weights))]
    return knapsack_recursive_dp_top_down(weights, profits, capacity, 0, dp)



def knapsack_recursive_dp_top_down(weights, profits, capacity, index, dp):
    if capacity <= 0 or index >= len(weights):
        return 0
    if dp[index][capacity] != -1:
        return dp[index][capacity]
    p1 = 0
    if weights[index] <= capacity:
        p1 = profits[index] + knapsack_recursive_dp_top_down(weights, profits, capacity - weights[index], index + 1, dp)
    p2 = knapsack_recursive_dp_top_down(weights, profits, capacity, index + 1, dp)

    dp[index][capacity] = max(p1, p2)
    return dp[index][capacity]


def print_selected_elements(dp, weights, profits, capacity):
    n = len(weights)
    total_profit = dp[-1][-1]
    for i in range(n-1, 0, -1):
        if total_profit != dp[i-1][capacity]:
            print(weights[i], end=" ")
            capacity -= weights[i]
            total_profit -= profits[i]
    if total_profit != 0:
        print(weights[0])
    print("are the selected elements")
    return

def knapsack_using_dp_bottom_up(weights, profits, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [[0 for i in range(capacity + 1)] for j in range(len(weights))]
    # Time complexity = O(N*C)
    # space Complexity = O(N*C)
    for c in range(capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    n = len(weights)
    for i in range(1, n):
        for c in range(1, capacity+1):
            p1,p2 = 0, 0
            if weights[i] <= c:
                p1 = profits[i]+ dp[i-1][c-weights[i]]
            p2  = dp[i-1][c]
            dp[i][c] = max(p1, p2)
    print_selected_elements(dp, weights, profits, capacity)
    return dp[-1][-1]



def knapsack_using_dp_bottom_up_space_optimized(weights, profits, capacity):
    """
    Time complexity = O(N *C)
    Space complexity = O(2*C)
    """
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [[0 for i in range(capacity + 1)] for j in range(2)]
    for c in range(capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]
    for i in range(1, n):
        for c in range(1, capacity + 1):
            p1, p2 = 0, 0
            if weights[i] <= c:
                p1 = profits[i] + dp[(i - 1)%2][c - weights[i]]
            p2 = dp[(i - 1)%2][c]
            dp[i%2][c] = max(p1, p2)
    return dp[(n-1)%2][capacity]



def knapsack_using_dp_bottom_up_1D_optimized(weights, profits, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    dp = [0 for x in range(capacity+1)]
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
    return dp[capacity]








profits = [1, 6, 10, 16]
weights = [1, 2, 3, 5]
capacity = 7
print(knapsack(weights, profits, capacity))
print(knapsack_using_dp_top_down(weights, profits, capacity))
print(knapsack_using_dp_bottom_up(weights, profits, capacity))
print(knapsack_using_dp_bottom_up_space_optimized(weights, profits, capacity))
print(knapsack_using_dp_bottom_up_1D_optimized(weights, profits, capacity))
