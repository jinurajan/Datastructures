"""
Given a list of weights [w1,w2,...,wn], determine all sums that can be constructed using the weights. For example, if the weights are [1,3,3,5], the following sums are possible:
"""


# for (int k = 1; k <= n; k++) {
# for (int x = 0; x <= W; x++) {
# if (x-w[k] >= 0) possible[x][k] |= possible[x-w[k]][k-1]; possible[x][k] |= possible[x][k-1];
# } }

def possible_sums(weights):
    n = len(weights)
    W = sum(weights) + 1
    dp = [[0 for i in range(W)] for j in range(n)]
    w = [i for i in range(max(weights))]
    print(dp)
    for x in range(1, W):
        for k in range(n):
            # print(x, weights[k])
            if x - w[k] >=0:
                print(x, w[k])
                dp[x][k] |= dp[x-w[k]][k-1]
            dp[x][k] |= dp[x][k-1]
    print(dp)
weights = [1,3,3, 5]
print(possible_sums(weights))
