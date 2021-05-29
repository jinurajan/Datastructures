"""
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""


def find_subsets(nums):
    subsets = []
    n = len(nums)
    subset = []

    def backtrack(index):
        if index == n:
            subsets.append(subset[:])
            return
        backtrack(index + 1)
        subset.append(nums[index])
        backtrack(index + 1)
        subset.pop()

    backtrack(0)
    return subsets

def find_subsets(nums):
  subsets = []
  n = len(nums)
  subset = []
  def backtrack(index):
    if index == n:
      subsets.append(subset[:])
      return
    subset.append(nums[index])
    backtrack(index+1)
    subset.pop()
    backtrack(index+1)

  backtrack(0)
  return subsets


def find_subsets(nums):
  subsets = [[]]
  for num in nums:
    n = len(subsets)
    for i in range(n):
      subset = list(subsets[i])
      subset.append(num)
      subsets.append(subset)
  return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
