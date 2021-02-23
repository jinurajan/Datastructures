"""
Generating Permutations

Method1: Using Recursion / backtracking
"""


from collections import defaultdict

def generate_permutations_1(array):
    n = len(array)
    results = []
    visited = defaultdict(lambda: False)
    combination = []
    def backtrack(combination):
        if len(combination) == n:
            results.append(combination[:])
        else:
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                combination.append(array[i])
                backtrack(combination)
                visited[i] = False 0-====
                combination.pop()
    backtrack(combination)
    return results

from itertools import permutations

def generate_permutations_2(array):
    """ Using pythons inbuilt permutations"""
    result = []
    for perm in permutations(array):
        result.append(list(perm))
    return result




array = [1,2,3]
print(generate_permutations_1(array))
print(generate_permutations_2(array))