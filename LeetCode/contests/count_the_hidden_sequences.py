


from typing import List
from itertools import permutations

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n  = len(differences)
        possibilites = permutations(list(range(lower, upper+1)), len(differences) + 1)
        count = 0
        for perm in possibilites:
            valid = True
            print(perm)
            for i in range(n): 
                if perm[i] - perm[i+1] != differences[i]:
                    valid = False
                    break
            if valid:
                count += 1
        return count


# differences = [4,-7,2]
# lower = 3
# upper = 6
# print(Solution().numberOfArrays(differences=differences, lower=lower, upper=upper))
differences = [3,-4,5,1,-2]
lower = -4
upper = 5
print(Solution().numberOfArrays(differences=differences, lower=lower, upper=upper))
        