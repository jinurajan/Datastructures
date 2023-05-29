"""
Given a sorted integer array nums and two integers—k and num—return the k closest integers to num in this array. Ensure that the result is sorted in ascending order.

The integer a is closer to num than an integer b if the following are true:

|a - num| < |b - num|, or
|a - num| = |b - num| and a < b

Constraints:

1 ≤ k ≤ nums.length
1 ≤ nums.length <= pow(10, 4)

nums is sorted in ascending order
-pow(10, 4) <= nums[i, num <= pow(10, 4)
"""

def bs(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low+high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return low


def find_closest_elements(nums, k, num):
    # left is left of the starting element
    # right is not included in the k hence right-left-1 = k
    if len(nums) == k:
        return nums
    
    right = bs(nums, num)
    left = right-1

    while right-left-1 < k:
        if left == -1:
            right += 1
            continue
        if right == len(nums) or abs(nums[left]- num) <= abs(nums[right]-num):
            left -= 1
        else:
            right +=1
    return nums[left+1:right]


# Driver code
def main():

    nums = [
                [1, 2, 3, 4, 5, 6, 7],
                [1, 2, 3, 4, 5],
                [1, 2, 4, 5, 6],
                [1, 2, 3, 4, 5, 10]
                ]
    k = [4, 4, 2, 3]
    num = [4, 3, 10, -5]
    for i in range(len(nums)):
        print((i + 1), ".\tThe ", k[i],
              " Closest Elements for the number ", num[i], " in the array ",
              nums[i], " are:", sep="")
        print("\t", find_closest_elements(nums[i], k[i], num[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
