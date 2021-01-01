"""
H-Index
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has index h if h of his/her N papers have at least h citations each, and the other N-h papers have no more than h citations each.
Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.


"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0

        citations = sorted(citations, reverse=True)
        # h_index range is in between min(citations) and max(citations)
        n = len(citations)-1
        while n >= 0:
            if citations[n] >= n+1:
                return n+1
            n -= 1
        return 0



if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print Solution().hIndex(citations) == 3
    citations = [7,6,5,4,3,2,1]
    print Solution().hIndex(citations) == 4
    citations = [25, 8, 5, 3, 3]
    print Solution().hIndex(citations) == 3
    citations = [11, 15]
    print Solution().hIndex(citations) == 2
    citations = [100]
    print Solution().hIndex(citations) == 1
    citations = [0, 0]
    print Solution().hIndex(citations) == 0
    citations = [0, 1]
    print Solution().hIndex(citations) == 1
