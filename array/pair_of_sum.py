"""given an array A[] of n numbers and another number x, determines whether or not there exist 
two elements in S whose sum is exactly
"""



""" uses sorting and comparison together
i have used python buitin method to sort go for any algos which use O(nlogn)
total complexity is O(nlogn)+O(n) ~ O(n)
"""

def find_pair_of_sum(array, sum_value, result):
	# sort the array using any nlogn algos
	sorted_array = sorted(array)
	lb = 0
	rb = len(array)-1
	while lb < rb:
		s = sorted_array[lb]+sorted_array[rb]
		if s == sum_value:
			result.append((sorted_array[lb], sorted_array[rb]))
			lb = lb+1
			rb = rb-1
		elif s  < sum_value:
			lb +=1
		else:
			rb -=1
	return result

"""
	Uses a large array as bitmap where values are all 0 initially
	find sum-array[i] and if its there in binmap add to result array
	else set the binmap as 1
	Complexity would be O(n) for iteration and O(n) for space
"""
CONST_MAX = 100000

def find_pair_of_sum_using_binmap(array, sum_value, result):

	binmap = [0]*CONST_MAX
	for i in range(len(array)):
		temp = sum_value - array[i]
		if temp >=0 and  binmap[temp] ==1 :
			result.append((array[i], temp))
		binmap[array[i]]=1
	return result






if __name__ == "__main__":
	array = [10,8,2,3,4,6,7]
	result = []
	print find_pair_of_sum(array, 10, result)
	result = []
	print find_pair_of_sum_using_binmap(array, 10, result)