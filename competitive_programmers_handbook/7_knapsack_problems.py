"""
Given a list of weights [w1,w2,...,wn], determine all sums that can be constructed using the weights. For example, if the weights are [1,3,3,5], the following sums are possible:
"""


# for (int k = 1; k <= n; k++) {
# for (int x = 0; x <= W; x++) {
# if (x-w[k] >= 0) possible[x][k] |= possible[x-w[k]][k-1]; possible[x][k] |= possible[x][k-1];
# } }
def possible_sums(weights):
    max_sum = sum(weights)+ 1
    w = len(weights)
    possible =[0 for i in range(max_sum)]
    possible[0] = 1
    for k in range(w):
        for x in range(max_sum-1, -1, -1):
            if possible[x]:
                possible[x+weights[k]] = 1
    result = [idx for idx, n in enumerate(possible) if n==1 and idx!=0]
    return result







weights = [1,3,3, 5]
print(possible_sums(weights))
