"""
Find the sum of array using recursion
1. Tail recursion
2. non Tail recursion

"""



def sum_non_tail_recursion(nums):
	if len(nums) == 0:
		return 0
	return nums[0] + sum_non_tail_recursion(nums[1:])



def sum_with_tail_recursion(nums):

	def helper(nums, s):
		if len(nums) == 0:
			return s
		return helper(nums[1:], nums[0]+ s)

	return helper(nums, 0)




array = [1, 2, 3, 4, 5]
print sum_non_tail_recursion(array)
print sum_with_tail_recursion(array)