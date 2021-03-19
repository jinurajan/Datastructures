"""
Next we consider the problem of generating all permutations of a set of n elements. For example, the permutations of {1, 2, 3} are (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), and (3, 2, 1).
"""

def generate_permutations(array):
    n = len(array)
    chosen = [False] * n
    result = []
    def search():
        if len(permutation) == n:
            result.append(permutation[:])
            return
        for i in range(n):
            if chosen[i]:
                continue
            chosen[i] = True
            permutation.append(array[i])
            search()
            chosen[i] = False
            permutation.pop()
    permutation = []
    search()
    return result

def generate_permutations(nums):
    n = len(nums)
    results = []

    def backtrack(first):
        if first == n:
            results.append(nums[:])
        else:
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
    backtrack(0)
    return results


print(generate_permutations([1,2,3]))