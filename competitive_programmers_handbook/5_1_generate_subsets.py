


def generate_subsets_1(array):
    """
    O(2 raised to n)
    """
    n = len(array)
    subset = []
    results = []
    def backtrack(k):
        if k == n:
            results.append(subset[:])
        else:
            backtrack(k+1)
            subset.append(array[k])
            backtrack(k+1)
            subset.pop()
    backtrack(0)
    return results


def generate_subsets_2(array):
    """
    Using bit representation. suppose if there are n element array
    consider n bit and toggle each one of it and use it as reference
    to build up the subset. for eg: if n = 3 and array is [1,2,3]
    000 -> []
    001 -> [1]
    010 -> [2]
    011 -> [1, 2]
    100 -> [3]
    101 -> [3, 1]
    110 -> [3, 2]
    111 -> [1, 2, 3]
    """
    n = len(array)
    b = 0
    results = []
    while b < (1<< n):
        subset = []
        for i in range(n):
            print(1 if b & (1 << i) else 0, end=",")
            if b & (1 << i):
                subset.append(array[i])
        print("\n")
        results.append(subset)
        b += 1
    return results




array = [1,2,3]
print(generate_subsets_1(array))
print(generate_subsets_2(array))
