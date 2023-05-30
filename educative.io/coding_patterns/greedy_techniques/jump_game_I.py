"""
In a single-player jump game, the player starts at one end of a series of squares, with the goal of reaching the last square.

At each turn, the player can take up to s steps towards the last square, where s is the value of the current square.

For example, if the value of the current square is 3,  the player can take either 3 steps or 2 steps or 1 step
 
step in the direction of the last square. The player cannot move in the opposite direction, that is, away from the last square.

You have been tasked with writing a function to validate whether a player can win a given game or not.

You have been provided with the nums integer array, representing the series of squares. The player starts at the first index and, following the rules of the game, tries to reach the last index.

If the player can reach the last index, your function returns TRUE; otherwise, it returns FALSE.

1 <= nums.length <= pow(10,3)
0 <= nums[i] <= pow(10, 3)
"""

def jump_game(nums):
    target_idx = len(nums)-1
    for i in range(len(nums)-2, -1, -1):
        if target_idx <= i + nums[i]:
            target_idx = i
    if target_idx == 0:
        return True
    return False
   

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
        print("\tCan we reach the very last index? ",
              "True" if jump_game(nums[i]) else "False", sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()


