"""
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.

"""
from collections import deque


def find_permutations(nums):
  result = []
  n = len(nums)
  def backtrack(index):
    if index == n:
      result.append(nums[:])
      return
    for i in range(index, n):
      nums[index],nums[i] = nums[i], nums[index]
      backtrack(index+1)
      nums[index],nums[i] = nums[i], nums[index]
  backtrack(0)
  return result

def find_permutations1(nums):
    n = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for num in nums:
        n = len(permutations)
        for _ in range(n):
            old_perm = permutations.popleft()
            for j in range(len(old_perm)+1):
                new_perm = list(old_perm)
                new_perm.insert(j, num)
                if len(new_perm) == n:
                    result.append(new_perm)
                else:
                    permutations.append(new_perm)
    return result


def main():
  print("Here are all the permutations: " + str(find_permutations1([1, 3, 5])))


main()
