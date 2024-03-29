
def generate_permutations(array):
	n = len(array)
	result = []
	idx_map = [0 for i in range(n)]
	def backtrack(perm):
		if len(perm) == n:
			result.append(perm[:])
			return
		for i in range(n):
			if idx_map[i]:
				continue
			idx_map[i] = 1
			perm.append(array[i])
			backtrack(perm)
			idx_map[i] = 0
			perm.pop()
	backtrack([])
	return result


def generate_permutations(array):
	n = len(array)
	result = []
	def search(first):
		if first == n:
			result.append(array[:])
			return
		for i in range(first, n):
			array[first], array[i] = array[i], array[first]
			search(first+1)
			array[first], array[i] = array[i], array[first]
	search(0)
	return result


print(generate_permutations([1,2,3]))





