

def bin_search(array, start, end, index):
	if(end >start):
		mid = (start+end)/2
		if array[mid] >= array[mid-1] and array[mid+1] <= array[mid]:
			if index != -1:
				if array[index] > array[mid]: 
					return index
				else:
					return mid
			else:
				return mid
		if array[mid+1] > array[mid]:
			# lies on on right side
			return bin_search(array, mid+1, end, index)
		else:
			return bin_search(array, 0, mid-1, index)
	return -99

def  findTurningIndex(input):
    return bin_search(input, 0, len(input), -1)
		



if __name__ == "__main__":
	input = [8,9,12,4,3,8,9,14,4,3]
	print findTurningIndex(input)