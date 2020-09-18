"""
K-th Symbol in Grammar

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
row 5: 01101001 10010100
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].

a = 0 b = 1
row 1 = 0                                       length = 1
row 2 = ab                                      length = 2
row 3 = ab ba                                   length = 4
row 4 = abba baab                               length = 8
row 5 = abbabaab baababba                       length = 16
row 6 = abbabaab baababba  baababba abbabaab    length = 32 ie 2 raised row-1 ie 2 raised to 5

and so on 

1) 
    KthGrammer(N, K) = K-1thGrammer(N-1, K//2)

    for eg N = 4 and K = 3

    KthGrammer(4, 3) = K-1thGrammer(N-1, K//2) 3 < 2 raised to 3 
                 = abba = b

    Ans is B
2) if number of 1's in K-1 is even ans 0 else 1 


K = 1 K-1 = 0 number of 1s is 0 hence 0
K = 2 K-1 =1 number of 1s is 1 hence 1
K = 3 K-1 = 2 number of 1s is 1 hence 1
K = 4 K-1 = 3 = 0011 = number of 1s is 2 hence 0
K = 5 K-1 = 4 0100 number of 1s is 1 hence 1
"""
from math import ceil

class Solution1(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        return bin(K - 1).count('1') % 2



class Solution2(object):
    def kthGrammar(self, n, k):
        def f(n,k):
            if n==1:
                return k^1
            l=1<<(n-2)
            if k>l:
                return f(n-1,k-l)^1
            return f(n-1,k)
        return f(n,k)


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 0:
            return 0
        r = self.kthGrammar(N-1, ceil((K+1)//2))
        """
        0110 is the least possible
        position wise
        if r == 0
            1 - 0 k = 1 mean 0th position which is 0
            2 - 1 k = 2 means 1st position which is 1
        if r == 1:
            3 - 1 k = 3 means 2nd position which is 1
            4 - 0 k = 4 means 3rd position which is 0
        """ 
        if r == 0:
            if K % 2 == 1:
                return 0
            else:
                return 1
        else:
            if K % 2 == 1:
                return 1
            else:
                return 0



print Solution().kthGrammar(1, 1) # 0
print Solution().kthGrammar(2, 1) # 0
print Solution().kthGrammar(2, 2) # 1
print Solution().kthGrammar(4, 5) # 1
print Solution().kthGrammar(4, 6) # 0
print Solution().kthGrammar(4, 8)  #1
print Solution().kthGrammar(3, 3)  # 1
print "*************************"
print Solution1().kthGrammar(1, 1) # 0
print Solution1().kthGrammar(2, 1) # 0
print Solution1().kthGrammar(2, 2) # 1
print Solution1().kthGrammar(4, 5) # 1
print Solution1().kthGrammar(4, 6) # 0
print Solution1().kthGrammar(4, 8)  #1
print Solution1().kthGrammar(3, 3)  # 1
print "*************************"
print Solution2().kthGrammar(1, 1) # 0
print Solution2().kthGrammar(2, 1) # 0
print Solution2().kthGrammar(2, 2) # 1
print Solution2().kthGrammar(4, 5) # 1
print Solution2().kthGrammar(4, 6) # 0
print Solution2().kthGrammar(4, 8)  #1
print Solution2().kthGrammar(3, 3)  # 1

