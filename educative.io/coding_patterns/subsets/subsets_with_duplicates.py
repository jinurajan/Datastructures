"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:

Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]
Example 2:

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]

"""


def find_subsets(nums):
  nums.sort()
  n = len(nums)
  subsets = [[]]
  start, end = 0, 0
  for i in range(n):
    start = 0
    if i > 0 and nums[i] == nums[i-1]:
      start = end + 1
    end = len(subsets) - 1
    for j in range(start, end+1):
      subset = list(subsets[j])
      subset.append(nums[i])
      subsets.append(subset)
    print(subsets)
  return subsets


def find_subsets_1(nums):
  subsets = []
  visited = set()
  n = len(nums)
  for b in range((1 << n)):
    subset = []
    for i in range(n):
      if b & (1 << i):
        subset.append(nums[i])
    if tuple(sorted(subset)) not in visited:
      subsets.append(subset)
    visited.add(tuple(sorted(subset)))
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  # print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
