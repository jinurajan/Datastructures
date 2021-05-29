"""
Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.
Input: "abdbca"
Output: 3
Explanation: LPS is "bdb".

Input: = "cddpd"
Output: 3
Explanation: LPS is "dpd".

Input: = "pqr"
Output: 1
Explanation: LPS could be "p", "q" or "r".

"""

def find_LPS_length(st):
    """
    Time complexity : O(3 raised to N)
    Space Complexity: O(N) for recursive calls
    """
    return find_LPS_length_recursive(st, 0, len(st)-1)


def find_LPS_length_recursive(st, start, end):
    if start > end:
        return 0
    if start == end:
        return 1
    if st[start] == st[end]:
        # check if remaining is palindrome
        remaining = end - start - 1
        if find_LPS_length_recursive(st, start+1, end-1) == remaining:
            return remaining + 2

    c1 = find_LPS_length_recursive(st, start+1, end)
    c2 = find_LPS_length_recursive(st, start, end-1)
    return max(c1, c2)


def find_LPS_length_top_bottom(st):
    """
    Time = O(N**2)
    Space = O(N**2)
    """
    n = len(st)
    dp =[[-1 for _ in range(n)] for _ in range(n)]

    def find_LPS_length(st, start, end):
        if start > end:
            return 0
        if start == end:
            return 1
        if dp[start][end] == -1:
            if st[start] == st[end]:
                remaining = end-start-1
                if find_LPS_length(st, start+1, end-1) == remaining:
                    dp[start][end] = remaining + 2
                    return dp[start][end]
            c1 = find_LPS_length(st, start+1, end)
            c2 = find_LPS_length(st, start, end-1)
            dp[start][end] = max(c1, c2)
        return dp[start][end]

    return find_LPS_length(st, 0, n-1)



def find_LPS_length_bottom_up(st):
    n = len(st)
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    max_len = 1
    for start in range(n-1, -1, -1):
        for end in range(start+1, n):
            if st[start] == st[end]:
                # if left is two character / remaining is palindrome
                if end-start == 1 or dp[start+1][end-1]:
                    dp[start][end] = True
                    max_len = max(max_len, end-start+1)
    return max_len

def find_LPS_length_manachers_algorithm(st):
    # pick possible middle of palindrome and check both left and right to find the length
    pass



print(find_LPS_length("abdbca"))
print(find_LPS_length("cddpd"))
print(find_LPS_length("pqr"))


print(find_LPS_length_top_bottom("abdbca"))
print(find_LPS_length_top_bottom("cddpd"))
print(find_LPS_length_top_bottom("pqr"))


print(find_LPS_length_bottom_up("abdbca"))
print(find_LPS_length_bottom_up("cddpd"))
print(find_LPS_length_bottom_up("pqr"))