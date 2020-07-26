"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        else:
            hash_set = set()
            start_index = 0
            end_index = 0
            insert_index = 1
            for i in range(len(nums)):
                if nums[i] not in hash_set:
                    # new element in the array
                    start_index = i
                    hash_set.add(nums[i])
                    if start_index != end_index:
                        nums[insert_index] = nums[i]
                        insert_index += 1
                else:
                    end_index = i
        return len(hash_set)


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums1 = [1, 1, 2]
    nums2 = [1, 1, 2, 3]
    nums3 = [1, 2, 2, 3]
    print(Solution().removeDuplicates(nums))
    print(Solution().removeDuplicates(nums1))
    print(Solution().removeDuplicates(nums2))
    print(Solution().removeDuplicates(nums3))
