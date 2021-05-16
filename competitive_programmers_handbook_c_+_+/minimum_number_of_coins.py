




def find_min_number_of_coins(coins, target):
    dp = [float("inf") for i in range(target+1)]
    dp[0] = 0
    for i in range(1, target+1):
        for coin in coins:
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[-1]

def find_min_number_of_coins_1(coins, target):
    dp = [float("inf") for i in range(target+1)]
    dp[0] = 0
    for i in range(1, target+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[-1]


def count_number_of_solutions(coins, target):
    dp = [0 for i in range(target+1)]
    dp[0] = 1
    for i in range(1, target+1):
        for coin in coins:
            if i-coin >= 0:
                dp[i] += dp[i-coin]
    print(dp)
    return dp[-1]

coins = {1, 3, 4}
target = 6
print(find_min_number_of_coins(coins, target))
print(find_min_number_of_coins_1(coins, target))
print(count_number_of_solutions(coins, target))
print(count_number_of_solutions(coins, 5))

