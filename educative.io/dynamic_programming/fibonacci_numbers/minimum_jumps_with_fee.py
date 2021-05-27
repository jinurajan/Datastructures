"""
Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that you have to pay if you take the step. Implement a method to calculate the minimum fee required to reach the top of the staircase (beyond the top-most step). At every step, you have an option to take either 1 step, 2 steps, or 3 steps. You should assume that you are standing at the first step.

Number of stairs (n) : 6
Fee: {1,2,5,2,1,2}
Output: 3
Explanation: Starting from index '0', we can reach the top through: 0->3->top
The total fee we have to pay will be (1+2).
Example 2:

Number of stairs (n): 4
Fee: {2,3,4,5}
Output: 5
Explanation: Starting from index '0', we can reach the top through: 0->1->top
The total fee we have to pay will be (2+3).
"""

def find_min_fee(fee):
    return find_min_fee_recursive(fee, 0, len(fee))


def find_min_fee_recursive(fee, index, n):
    if index >= n:
        # reached on top
        return 0

    return min(find_min_fee_recursive(fee, index+1, n),
               find_min_fee_recursive(fee, index+2, n),
               find_min_fee_recursive(fee, index+3, n)) + fee[index]


def find_min_fee_top_down(fee):
    n = len(fee)
    dp = [0 for i in range(n)]

    def find_min(index):
        if index > n-1:
            return 0
        if dp[index] == 0:
            dp[index] = min(find_min_fee_recursive(fee, index+1, n),
               find_min_fee_recursive(fee, index+2, n),
               find_min_fee_recursive(fee, index+3, n)) + fee[index]
        return dp[index]

    return find_min(0)


def find_min_fee_bottom_up(fee):
    n = len(fee)
    dp = [0 for i in range(n+1)]
    dp[1] = fee[0]
    dp[2] = fee[0]
    for i in range(2, n):
        dp[i+1] = min(
            fee[i] + dp[i],
            fee[i-1] + dp[i-1],
            fee[i-2] + dp[i-2]
        )
    return dp[n]

print(find_min_fee([1, 2, 5, 2, 1, 2]))
print(find_min_fee([2, 3, 4, 5]))

print(find_min_fee_top_down([1, 2, 5, 2, 1, 2]))
print(find_min_fee_top_down([2, 3, 4, 5]))

print(find_min_fee_bottom_up([1, 2, 5, 2, 1, 2]))
print(find_min_fee_bottom_up([2, 3, 4, 5]))

