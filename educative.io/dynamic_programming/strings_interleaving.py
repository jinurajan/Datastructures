"""
Give three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ has been formed by interleaving ‘m’ and ‘n’. ‘p’ would be considered interleaving ‘m’ and ‘n’ if it contains all the letters from ‘m’ and ‘n’ and the order of letters is preserved too.

Example 1:

Input: m="abd", n="cef", p="abcdef"
Output: true
Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.
Example 2:

Input: m="abd", n="cef", p="adcbef"
Output: false
Explanation: 'p' contains all the letters from 'm' and 'n' but does not preserve the order.
Example 3:

Input: m="abc", n="def", p="abdccf"
Output: false
Explanation: 'p' does not contain all the letters from 'm' and 'n'.
Example 4:

Input: m="abcdef", n="mnop", p="mnaobcdepf"
Output: true
Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.

"""

def find_SI(m, n,  p):
    return find_SI_recursive(m, n, p, 0, 0, 0)

def find_SI_recursive(m, n, p, m_idx, n_idx, p_idx):
    m_len, n_len, p_len = len(m), len(n), len(p)
    if m_idx == m_len and n_idx == n_len and p_idx == p_len:
        return True
    if p_idx == p_len:
        return False
    b1, b2 = False, False
    if m_idx < m_len and m[m_idx] == p[p_idx]:
        b1 = find_SI_recursive(m, n, p,m_idx+1, n_idx, p_idx+1)
    if n_idx < n_len and n[n_idx] == p[p_idx]:
        b2 = find_SI_recursive(m, n, p, m_idx, n_idx+1, p_idx+1)
    return b1 or b2


def find_SI_topdown(m, n,  p):
    return find_SI_recursive_topdown({}, m, n, p, 0, 0, 0)


def find_SI_recursive_topdown(dp, m, n, p, m_idx, n_idx, p_idx):
    m_len, n_len, p_len = len(m), len(n), len(p)
    if m_idx == m_len and n_idx == n_len and p_idx == p_len:
        return True
    if p_idx == p_len:
        return False
    key = f"{m_idx}{n_idx}{p_idx}"
    if key not in dp:
        b1, b2 = False, False
        if m_idx < m_len and m[m_idx] == p[p_idx]:
            b1 = find_SI_recursive(m, n, p, m_idx + 1, n_idx, p_idx + 1)
        if n_idx < n_len and n[n_idx] == p[p_idx]:
            b2 = find_SI_recursive(m, n, p, m_idx, n_idx + 1, p_idx + 1)
        dp[key] = b1 or b2
    return dp[key]



def find_SI_bottomup(m, n, p):
    m_len , n_len ,p_len = len(m), len(n), len(p)
    dp = [[False for _ in range(n_len+1)] for _ in range(m_len+1)]
    if m_len + n_len != p_len:
        return False
    for m_idx in range(m_len+1):
        for n_idx in range(n_len+1):
            if m_idx == 0 and n_idx == 0:
                dp[m_idx][n_idx] = True
            elif m_idx == 0 and n[n_idx-1] == p[m_idx+n_idx-1]:
                dp[m_idx][n_idx] = dp[m_idx][n_idx-1]
            elif n_idx == 0 and m[m_idx-1] == p[m_idx+n_idx-1]:
                dp[m_idx][n_idx] = dp[m_idx-1][n_idx]
            else:
                if m_idx > 0 and m[m_idx-1] == p[m_idx+n_idx-1]:
                    dp[m_idx][n_idx] = dp[m_idx-1][n_idx]
                if n_idx > 0 and n[n_idx-1] == p[m_idx+n_idx-1]:
                    dp[m_idx][n_idx] |= dp[m_idx][n_idx - 1]
    return dp[m_len][n_len]






    return find_SI_recursive_topdown({}, m, n, p, 0, 0, 0)

print(find_SI("abd", "cef", "abcdef"))
print(find_SI("abd", "cef", "adcbef"))
print(find_SI("abc", "def", "abdccf"))
print(find_SI("abcdef", "mnop", "mnaobcdepf"))
print("")


print(find_SI_topdown("abd", "cef", "abcdef"))
print(find_SI_topdown("abd", "cef", "adcbef"))
print(find_SI_topdown("abc", "def", "abdccf"))
print(find_SI_topdown("abcdef", "mnop", "mnaobcdepf"))
print("")
print(find_SI_bottomup("abd", "cef", "abcdef"))
print(find_SI_bottomup("abd", "cef", "adcbef"))
print(find_SI_bottomup("abc", "def", "abdccf"))
print(find_SI_bottomup("abcdef", "mnop", "mnaobcdepf"))
