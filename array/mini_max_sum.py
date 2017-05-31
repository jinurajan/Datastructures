


def MinMaxSum(array):
	max_sum = 0
	min_sum = 18446744073709551616
	s = 0
	n = len(array)
	for i in range(len(array)):
		s = sum(array[0:i])+sum(array[i+1:n])
		print s
		if max_sum < s:
			max_sum = s
		if min_sum > s:
			min_sum = s
	print min_sum, max_sum




if __name__== "__main__":
	array = [1,2,3,4,5]
	MinMaxSum(array)