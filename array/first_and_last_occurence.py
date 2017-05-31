



def first_and_last_occurence(array, start, end, key, first_index, last_index):
	if(start <= end):
		mid = (start+end)//2
		if array[mid] == key: 
			if first_index == -1 or  first_index > mid:
				first_index = mid
			if last_index == -1 or last_index < mid:
				last_index = mid;
			return first_and_last_occurence(array, start, mid-1, key, first_index, last_index);
		elif key > array[mid]:
			return first_and_last_occurence(array, mid+1, end, key, first_index,last_index );
		elif key < array[mid]:
			return first_and_last_occurence(array, lb, mid-1, key, first_index, last_index);
	return first_index, last_index;

	






if __name__ == "__main__":
	first_index = -1
	last_index = -1
	array = [1, 3, 5, 5, 5 ,67, 123, 125]
	key = 5
	print first_and_last_occurence(array, 0, len(array)-1, key, first_index, last_index)