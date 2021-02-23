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
                visited[i] = False
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



def generate_permutations_3(array):
    n = len(array)
    results = []
    def backtrack(first):
        if first == n:
            results.append(array[:])
        else:
            for i in range(first, n):
                array[first], array[i] = array[i], array[first]
                backtrack(first+1)
                array[first], array[i] = array[i], array[first]
    backtrack(0)
    return results


array = [1,2,3]
print(generate_permutations_1(array))
print(generate_permutations_2(array))
print(generate_permutations_3(array))