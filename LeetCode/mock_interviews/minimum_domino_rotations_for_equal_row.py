"""
Minimum Domino Rotations For Equal Row

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.


Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.


Constraints:

2 <= A.length == B.length <= 2 * 104
1 <= A[i], B[i] <= 6
"""


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        def find_rotations(x):
            rot_a, rot_b = 0, 0
            for i in range(n):
                if A[i] != x and B[i] != x:
                    return -1
                elif B[i] != x:
                    rot_b += 1
                elif A[i] != x:
                    rot_a += 1
            return min(rot_a, rot_b)

        n = len(A)
        rotations = find_rotations(A[0])
        if rotations != -1 or A[0] == B[0]:
            return rotations
        else:
            return find_rotations(B[0])