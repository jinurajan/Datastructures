# suppose there are only one step then number of ways: 1 -> (1)
#  if n = 2  (1,1) and (2)
#  if n = 3 (1,1,1) (1,2) (2,1)
#  if n = 4 (1,1,1,1) (2,2) (1,1,2), (2,1,1) (1,2,1) and so on




def fib(n):
	if n <=2:
		return 2
	return n+fib(n-1)


def main(n):
	if n ==0:
		return 0;
	else:
		return fib(n+1)

if __name__ == "__main__":
	print main(0)
	print main(1)
	print main(2)
	print main(3)
