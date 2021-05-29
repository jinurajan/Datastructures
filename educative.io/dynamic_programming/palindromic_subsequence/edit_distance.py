"""
Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting, or replacing characters. Write a function to calculate the count of the minimum number of edit operations.

Example 1:

Input: s1 = "bat"
       s2 = "but"
Output: 1
Explanation: We just need to replace 'a' with 'u' to transform s1 to s2.
Example 2:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: We can replace first 'a' with 'c' and delete second 'c'.
Example 3:

Input: s1 = "passpot"
       s2 = "ppsspqrt"
Output: 3
Explanation: Replace 'a' with 'p', 'o' with 'q', and insert 'r'.
"""
def find_min_operations(s1, s2):
    return find_min_operations_recursive(s1, s2, 0, 0)

def find_min_operations_recursive(s1, s2, i1, i2):
    n1, n2 = len(s1), len(s2)
    if i1 == n1:
        return n2-i2
    if i2 == n2:
        return n1 - i1
    if s1[i1] == s2[i2]:
        return find_min_operations_recursive(s1, s2, i1+1, i2+1)
    c1 = 1 + find_min_operations_recursive(s1, s2, i1, i2+1)
    c2 = 1 + find_min_operations_recursive(s1, s2, i1+1, i2)
    c3 = 1 + find_min_operations_recursive(s1, s2, i1+1, i2+1)

    return min(c1, c2, c3)

def find_min_operations_topdown(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]

    return find_min_operations_recursive_topdown(dp, s1, s2, 0, 0)

def find_min_operations_recursive_topdown(dp, s1, s2, i1, i2):
    n1, n2 = len(s1), len(s2)
    if i1 == n1:
        return n2 - i2
    if i2 == n2:
        return n1 - i1
    if dp[i1][i2] == -1 :
        if s1[i1] == s2[i2]:
            return find_min_operations_recursive_topdown(dp, s1, s2, i1 + 1, i2 + 1)
        c1 = 1 + find_min_operations_recursive_topdown(dp, s1, s2, i1, i2 + 1)
        c2 = 1 + find_min_operations_recursive_topdown(dp, s1, s2, i1 + 1, i2)
        c3 = 1 + find_min_operations_recursive_topdown(dp, s1, s2, i1 + 1, i2 + 1)
        dp[i1][i2] = min(c1, c2, c3)
    return dp[i1][i2]



def find_min_operations_bottomup(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1+1):
        dp[i][0] = i
    for j in range(n2+1):
        dp[0][j] = j

    for i in range(1, n1+1):
        for j in range(1,n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j-1],
                    dp[i-1][j],
                    dp[i-1][j-1]
                )
    return dp[n1][n2]



print(find_min_operations("bat", "but"))
print(find_min_operations("abdca", "cbda"))
print(find_min_operations("passpot", "ppsspqrt"))


print(find_min_operations_topdown("bat", "but"))
print(find_min_operations_topdown("abdca", "cbda"))
print(find_min_operations_topdown("passpot", "ppsspqrt"))


print(find_min_operations_bottomup("bat", "but"))
print(find_min_operations_bottomup("abdca", "cbda"))
print(find_min_operations_bottomup("passpot", "ppsspqrt"))
