



def IsSumSubsets(array1, array2):
	if(sum(array1) == sum(array2)):
		return True
	return False


def subsets(array):
	for i in range(len(array)):
		front_array = array[:i]
		back_array = array[i+1:]
		if len(front_array) == len(back_array):
			print IsSumSubsets(front_array, back_array)
		


def main():
	array = [5,6,1,4,6,2,4]
	subsets(array)


if __name__ == "__main__":
	main()