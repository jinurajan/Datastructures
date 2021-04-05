def  generate_subsets_1(array):
    """
    In this backtracking method we first include the values and then exclude it
    hence the output will be
    [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]

    """
    n = len(array)
    subset = []
    results = []
    def backtrack(index):
        if index == n:
            results.append(subset[:])
            return
        subset.append(array[index])
        backtrack(index+1)
        subset.pop()
        backtrack(index+1)
    backtrack(0)
    return results

def generate_subsets_2(array):
    """
    In this backtracking method we first exclude the values and then include it
    hence the output will be
     [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
    """
    n = len(array)
    subset = []
    results = []
    def backtrack(index):
        if index == n:
            results.append(subset[:])
            return
        backtrack(index+1)
        subset.append(array[index])
        backtrack(index+1)
        subset.pop()
    backtrack(0)
    return results

def generate_subsets_3(array):
	n = len(array)
	results = []
	for b in range(1<<n):
		subset = []
		for i in range(n):
			if b & (1 <<i):
				subset.append(array[i])
		results.append(subset)
	return results




print(generate_subsets_1([1,2,3]))
print(generate_subsets_2([1,2,3]))
print(generate_subsets_3([1,2,3]))