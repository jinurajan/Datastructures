"""
In a non-empty array of integers, every number appears twice except for one, find that single number

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4
"""

def find_single_number(arr):
  rem = 0
  for num in arr:
    rem ^= num
  return rem

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()
