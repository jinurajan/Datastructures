"""
Given set of N integers find the triples where sum of triples are 0
"""


class Threesum(object):
	def count(self, nums):
		n = len(nums)
		count = 0
		for i in range(n):
			for j in range(i+1, n):
				for k in range(j+1, n):
					if nums[i] + nums[j] + nums[k] == 0:
						count += 1
		return count



print Threesum().count([30, -40, -20, -10, 40, 0, 10, 5])