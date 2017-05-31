



def find_peak_element(array, start, end):
	if start <= end:
		mid = (start+end)/2
		if (mid == 0 or array[mid-1] <= array[mid]) and (mid == end or array[mid+1] <= array[mid]):
			return array[mid]
		elif mid > 0 and (array[mid] < array[mid-1]):
			return find_peak_element(array, 0, mid-1)
		else:
			return find_peak_element(array, mid+1, end)


	return -1



if __name__ == "__main__":
	n = int(raw_input().strip())
	height = map(int,raw_input().strip().split(' '))
	peak_element = find_peak_element(array, 0, len(array)-1)
	print array.count(peak_element)
