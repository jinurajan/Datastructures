"""
Given a set of n positive integers, find all the possible subsets of integers that sum up to a number k.

1≤n≤10
1≤x≤100 where x is any member of the input set
1≤k≤pow(10, 3)
"""

def get_k_sum_subsets(set_of_integers, target_sum):
  # Write your code here
  subsets = set()
  n = len(set_of_integers)
  def backtrack(subset, index, sum):
    if index >= n:  
      if sum == target_sum:
        subsets.add(tuple(subset[:]))
      return
    
    if sum == target_sum:
        subsets.add(tuple(subset[:]))
    
    subset.append(set_of_integers[index])
    backtrack(subset, index+1, sum+set_of_integers[index])
    subset.pop()
    backtrack(subset, index+1, sum)
  backtrack([], 0, 0)
  return [list(subset) for subset in subsets]