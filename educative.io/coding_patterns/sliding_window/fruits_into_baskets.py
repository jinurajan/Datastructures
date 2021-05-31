"""
Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

"""

from collections import Counter


def fruits_into_baskets(fruits):
    n = len(fruits)
    left = 0
    right = 0
    baskets = Counter()
    max_len = float("-inf")
    while right < n:
        baskets[fruits[right]] += 1
        while len(baskets) > 2:
            baskets[fruits[left]] -= 1
            if baskets[fruits[left]] == 0:
                del baskets[fruits[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
        right += 1
    return -1 if max_len == float("-inf") else max_len

def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))

main()