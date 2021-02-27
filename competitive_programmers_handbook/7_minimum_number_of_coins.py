"""
Given a set of coin values coins={c1,c2,...,ck} and a target sum of money n, our task is to form the sum n using as few coins as possible.

"""
from collections import defaultdict



def min_no_of_coins_1(x):
    coins = {1,3,4}
    value = [0 for i in range(x+1) ]
    for i in range(1, x+1):
        value[i] = float("inf")
        for c in coins:
            if i-c >=0:
                value[i] = min(value[i], value[i-c]+1)
    return value[-1]


def min_no_of_coins_values(x):
    coins = [1, 3, 4]
    T = [float("inf") for i in range(x + 1)]
    result = [-1 for i in range(x+1)]
    T[0] = 0
    for j in range(len(coins)):
        for i in range(1, x+1):
            if i >= coins[j]:
                if T[i - coins[j]] + 1 < T[i]:
                    T[i] = 1 + T[i-coins[j]]
                    result[i] = j
    print_combinations(coins, result)
    return T[x]


def print_combinations(coins, result):
    if result[-1] == -1:
        print("no solution available")
    start = len(result) - 1
    while start !=0:
        j = result[start]
        print(coins[j], end=" ")
        start -= coins[j]
    print("\n")




def number_of_ways_with_backtrack(sum):
    count = 0
    coins = [1, 3, 4]
    def find_ways(x):
        nonlocal count
        if x == 0:
            count += 1
            return 1
        if x < 0:
            return 0
        s = 0
        for coin in coins:
            s += find_ways(x-coin)
        return s
    find_ways(sum)
    return count

def number_of_ways_with_dp(sum):
    coins = [1, 3, 4]
    count = [0 if i not in coins else 1 for i in range(sum+1) ]
    for i in range(1, sum+1):
        for c in coins:
            if i-c >=0:
                count[i] += count[i-c]
    return count[-1]


# x = 9
# print(min_no_of_coins_1(x) == 3)
# print(min_no_of_coins_values(x))
# x = 5
# print(min_no_of_coins_1(x) == 2)
# print(min_no_of_coins_values(x))
#
# x = 0
# print(min_no_of_coins_1(x) == 0)
# print(min_no_of_coins_values(x))
#
# x = 4
# print(min_no_of_coins_1(x) == 1)
# print(min_no_of_coins_values(x))

print(number_of_ways_with_backtrack(5))
print(number_of_ways_with_dp(5))