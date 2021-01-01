"""
Image Overlap

Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
"""


class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        l = len(A)
        c = len(A[0])
        result = 0
        for ro in range(-l, l+1):
            for co in range(-c, c+1):
                result = max(result, self.get_count(A, B, ro, co))
        return result

    def get_count(self, A, B, ro, co):
        rows = len(A)
        columns = len(A[0])
        count = 0
        for r in range(rows):
            for c in range(columns):
                if r + ro < 0 or r + ro >= rows or c + co < 0 or c + co >= columns:
                    continue
                if A[r + ro][c + co] == 1 and B[r][c] == 1:
                    count += 1
        return count


class Solution2(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        hash_set = set()
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j]:
                    hash_set.add((i,j))

    def get_count(self, A, hash_set, ro, co):
        rows = len(A)
        columns = len(A[0])
        count = 0
        for r in range(rows):
            for c in range(columns):
                if r + ro < 0 or r + ro >= rows or c + co < 0 or c + co >= columns:
                    continue
                if A[r + ro][c + co] and (r+ro,c+co) in hash_set:
                    count += 1
        return count




A = [[1,1,0],
     [0,1,0],
     [0,1,0]]

B = [[0,0,0],
     [0,1,1],
     [0,0,1]]

print Solution().largestOverlap(A, B)

A = [[1]]
B = [[1]]
print Solution().largestOverlap(A, B)

A = [[0,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,1,0,0,1]]
B = [[1,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[1,0,1,1,1]]
print Solution().largestOverlap(A, B)
