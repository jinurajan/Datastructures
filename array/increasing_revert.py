


def swap(input, i, j):
	print(i,j)
	temp = input[i]
	input[i] = input[j]
	input[j] = temp
	return input



def revertIt(input):
	span = 1
	n = len(input)
	i=0
	while i < n:
		if i+span-1 <= n-1:
			swap(input, i, i+span-1)
		print input
		span =span+1
		i = i+span-1
	print input






if __name__ == "__main__":
	input = [1,2,3,4,5,6,7,8]
	revertIt(input)