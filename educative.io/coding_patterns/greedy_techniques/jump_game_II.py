"""
In a single-player jump game, the player starts at one end of a series of squares, with the goal of reaching the last square.

At each turn, the player can take up to s steps towards the last square, where s is the value of the current square.

For example, if the value of the current square is 3, the player can take either 3 steps, or 2 steps, or 1 step in the direction of the last square. 
The player cannot move in the opposite direction, that is, away from the last square.

You have been provided with the nums integer array, representing the series of squares.

You are initially positioned at the first index of the array. Find the minimum number of jumps needed to reach the last index of the array.

You may assume that you can always reach the last index.

1 <= nums.length <= pow(10, 3)
0 <= nums[i] <= pow(10, 3)
"""


def jump_game_two(nums):
    # Your code will replace this placeholder return statement
    farthest_jump, current_jump, jumps = 0, 0, 0

    for i in range(len(nums)-1):
        farthest_jump = max(farthest_jump, i+nums[i])
        if i == current_jump:
            jumps += 1
            current_jump = farthest_jump

    return jumps

def main():
    nums = [
        [3, 2, 2, 0, 1, 4],
        [2, 3, 1, 1, 9],
        [3, 2, 1, 0, 4],
        [0],
        [1],
        [4, 3, 2, 1, 0],
        [1, 1, 1, 1, 1],
        [4, 0, 0, 0, 1],
        [3, 3, 3, 3, 3],
        [1, 2, 3, 4, 5, 6, 7]
    ]

    for i in range(len(nums)):
        print(i + 1, ".\tInput array: ", nums[i], sep="")
        print("\tMinimum Jumps Required to Reach end index: {}".format(jump_game_two(nums[i])))
        print("-" * 100)


if __name__ == '__main__':
    main()


