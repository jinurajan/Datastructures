

def binary_search(nums, target):
	if not nums:
		return -1
	l, r = 0, len(nums) -1
	while l < r:
		print(l, r)
		mid = (l + r) // 2
		if nums[mid] == target:
			return mid
		elif nums[mid] > target:
			r = mid
		else:
			l = mid + 1
	if l != len(nums) and nums[l] == target:
		return l
	return -1


print(binary_search([1, 2, 3, 4, 5, 7], 7))
# print(binary_search([1, 2, 3, 4, 5, 7], 1))
# print(binary_search([1, 2, 3, 4, 5, 7], 6))