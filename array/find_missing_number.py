#  find the missing number from a sorted array from 1 to n
# Note: Only one missing element is present




# Below solution uses sum of AP with difference as 1
#  find nth element in an AP is 2a+(n-1)d
#  complexity is O(n)
def find_missing_number_using_sum(array):
	n = len(array)
	# one element is missing so (n+1)*(n+2)/2
	total = (n+1)*(n+2)/2
	for i in range(0, n):
		total -= array[i]

	return total


# this uses binary search algorithm to search for missing element
# this works even if the elements are not starting from 1 but sorted
# and missing only one element
# Complexity: O(logn)

def find_missing_element_using_bs(array, start, end):
	if(end >= start):
		mid = (start+end)/2
		# assume that missing element lies on the left or right side of mid
		pre_diff = array[mid] - array[mid-1]
		post_diff = array[mid+1] - array[mid]

		if pre_diff > post_diff:
			return array[mid]-post_diff
		elif post_diff > pre_diff:
			return array[mid]+pre_diff
		else:
			# if both are equal it can lie on either left subarray or right sub array
			if array[mid]-start > end-array[mid]:
				# lies on the left subarray
				return find_missing_element_using_bs(array, 0, mid-1)
			else:
				return find_missing_element_using_bs(array, mid+1, end)
	return -1


# use XOR to find the missing element
# works for all sorted array
# Complexity is O(n) 
def find_missing_element_using_xor(array):
	x1 = array[0]
	x2 = array[0]
	n = len(array)
	for i in range(1, n):
		x1 = x1 ^ array[i]
	# change the limit to the last element value using 2a+(n-1)d if d is not 1
	for i in range(array[1], array[0]+n+1):
		x2 = x2 ^ i

	return x1 ^ x2




if __name__ == "__main__":
	array = [1,2,3,4,6,7,8,9,10]
	print find_missing_number_using_sum(array)
	print find_missing_element_using_bs(array, 0, len(array)-1)
	print find_missing_element_using_xor(array)
	array = [10,11,12,14,15,16,17]
	print find_missing_element_using_xor(array)