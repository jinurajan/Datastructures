"""
Find index of a key if it exists in a sorted array

Binary search recurrence

T(N) <= T(N/2) + 1 for N > 1 with T(1) = 1


"""

def binary_search_iter(nums, k):
	l = 0
	r = len(nums)-1
	while l <= r:
		mid = (l+r) / 2
		if nums[mid] > k:
			r = mid - 1
		elif nums[mid] < k:
			l = mid + 1
		else:
			return mid
	return -1


def binary_search(nums, k, l, r):
	if l <= r:
		mid = (l + r) / 2
		if nums[mid] == k:
			return mid
		if nums[mid] > k:
			return binary_search(nums, k, l, mid-1)
		else:
			return binary_search(nums, k, mid+1, r)
	return -1



print binary_search([1,2,3,4,5,6,7], 3, 0, 6)
print binary_search([1,2,3,4,5,6,7], 8, 0, 6)
print binary_search([6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97], 33, 0, 14)

print binary_search_iter([6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97], 97)
print binary_search([6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96], 96, 0, 13)
