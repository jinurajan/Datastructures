"""
An input array, nums containing non-zero integers, is given, where the value at each index represents the number of places to skip forward (if the value is positive) or backward (if the value is negative). When skipping forward or backward, wrap around if you reach either end of the array. For this reason, we are calling it a circular array. Determine if this circular array has a cycle. A cycle is a sequence of indices in the circular array characterized by the following:

The same set of indices is repeated when the sequence is traversed in accordance with the aforementioned rules.
The length of the sequence is at least two.
The loop must be in a single direction, forward or backward.
It should be noted that a cycle in the array does not have to originate at the beginning. A cycle can begin from any point in the array.

Constraints:

1
≤
1≤
 nums.length 
≤
1
0
4
≤10 
4

nums[i] 
!
=
0
!=0
"""



def circular_array_loop(nums):
    n = len(nums)

    for i in range(n):
        forward = nums[i] > 0
        slow = fast = i
        while True:
            slow = next_step(slow,  nums[slow], n)

            if is_not_cycle(nums, forward, slow):
                break

            fast = next_step(fast, nums[fast], n)
            if is_not_cycle(nums, forward, fast):
                break
            
            fast = next_step(fast, nums[fast], n)
            if is_not_cycle(nums, forward, fast):
                break

            if slow == fast:
                return True
    return False



def next_step(index, current_val, n):
    result = (index + current_val) % n
    if result < 0:
        result += n
    return result

def is_not_cycle(nums, prev_dir, index):
    curr_dir = nums[index] >= 0
    if (curr_dir != prev_dir) or (abs(nums[index] % len(nums)) == 0):
        return True
    return False


import pdb; pdb.set_trace()
input = (
    [-2, -3, -9],
    [-5, -4, -3, -2, -1],
    [-1, -2, -3, -4, -5],
    [2, 1, -1, -2],
    [-1, -2, -3, -4, -5, 6],
    [1, 2, -3, 3, 4, 7, 1],
    [2, 2, 2, 7, 2, -1, 2, -1, -1]
)
num = 1
for i in input:
    print(f"{num}.\tCircular array = {i}")
    print(f"\n\tFound loop = {circular_array_loop(i)}")
    print("-"*100, "\n")
    num += 1