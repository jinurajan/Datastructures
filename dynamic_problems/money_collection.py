



# def maxMoney(n, k):
# 	sum = 0
# 	for i in xrange(1, n+1):
# 		if k == 1:
# 			sum = 0;
# 		if sum+i == k:
# 			sum = sum+i-(i-1)
# 		else:
# 			sum = sum+i
# 	return sum


def find_index(n, k):
	sum = 0;
	for i in xrange(1, k/2):
		print("i: ", i)
		if sum+i == k:
			return i;
		else:
			sum = sum+i
		if sum >= k:
			return None



def maxMoney(n, k):
	total_possible_sum = (n*(n+1))/2
	if k > total_possible_sum:
		return total_possible_sum
	index = find_index(n, k)
	if not index:
		return total_possible_sum
	if index:
		return total_possible_sum-1
	else:
		return total_possible_sum - (index-1)



if __name__ == "__main__":
	n = 2
	k = 2
	# print maxMoney(3, 3)
	# print maxMoney(2, 1)
	print maxMoney(2000000, 3)