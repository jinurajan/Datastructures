"""
Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.

Example 2:

Input: s1: "abcf" s2:"bdcf"
Output: 5
Explanation: The shortest common super-sequence (SCS) is "abdcf".

Input: s1: "dynamic" s2:"programming"
Output: 15
Explanation: The SCS is "dynprogrammicng".
"""
def find_SCS_length(s1, s2):
  return find_SCS_length_recursive(s1, s2, 0, 0)

def find_SCS_length_recursive(s1, s2, i1, i2):
    n1, n2 = len(s1), len(s2)
    if i1 == n1:
        return n2 - i2
    if i2 == n2:
        return n1 - i1
    if s1[i1] == s2[i2]:
        return 1 + find_SCS_length_recursive(s1, s2, i1+1, i2+1)

    c1 = 1+ find_SCS_length_recursive(s1, s2, i1, i2+1)
    c2 = 1 + find_SCS_length_recursive(s1, s2, i1+1, i2)
    return min(c1, c2)


def find_SCS_length_topdown(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[-1 for _ in range(n2)] for _ in range(n1)]
    return find_SCS_length_topdown_recursive(dp, s1, s2, 0, 0)

def find_SCS_length_topdown_recursive(dp, s1, s2, i1, i2):
    n1, n2 = len(s1), len(s2)
    if i1 == n1:
        return n2 - i2
    if i2 == n2:
        return n1 - i1
    if dp[i1][i2] == -1:
        if s1[i1] == s2[i2]:
            return 1 + find_SCS_length_topdown_recursive(dp, s1, s2, i1 + 1, i2 + 1)

        c1 = 1 + find_SCS_length_topdown_recursive(dp, s1, s2, i1, i2 + 1)
        c2 = 1 + find_SCS_length_topdown_recursive(dp, s1, s2, i1 + 1, i2)
        dp[i1][i2] = min(c1, c2)
    return dp[i1][i2]


def find_SCS_length_bottomup(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1+1):
        dp[i][0] = i
    for j in range(n2+1):
        dp[0][j] = j

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]


print(find_SCS_length("abcf", "bdcf"))
print(find_SCS_length("dynamic", "programming"))

print(find_SCS_length_topdown("abcf", "bdcf"))
print(find_SCS_length_topdown("dynamic", "programming"))

print(find_SCS_length_bottomup("abcf", "bdcf"))
print(find_SCS_length_bottomup("dynamic", "programming"))
