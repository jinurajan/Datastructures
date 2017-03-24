


def fib(n):
	# time complexity : O(2**n)
	if n ==0:
		return 0;
	elif n <2:
		return 1
	else:
		return fib(n-1)+fib(n-2)


fib_values = {}

def fib_1_memoization(n):
	# time complexity : O(n)
	# space complexity: O(n)
	# Bottom up approach
	fib_values[0] = 0;
	fib_values[1] = 1;
	for i in range(2, n+1):
		fib_values[i] = fib_values[i-1]+fib_values[i-2]

	return fib_values[n]



if __name__ == "__main__":
	print fib(100)
	print fib_1_memoization(100)
	# print fib_top_down(5)