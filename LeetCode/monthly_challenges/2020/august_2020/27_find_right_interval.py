"""
"""


# class Solution(object):
#     def findRightInterval(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[int]
#         """
#         if len(intervals) == 0:
#             return []
#         elif len(intervals) == 1:
#             return [-1]
#         l = len(intervals)
#         hash_set = {tuple(intervals[i]): i for i in range(l)}
#         result = [-1] * l
#         intervals = sorted(intervals, key=lambda x: x[1])

#         for i in range(l):
#             for j in range(i, l):
#                 if intervals[j][0] >= intervals[i][1]:
#                     result[hash_set[tuple(intervals[i])]] = hash_set[tuple(intervals[j])]
#                     break
#         return result


class Solution(object):

    def find_interval(self, intervals, l, r):
        if l < r:
            

    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        if len(intervals) == 0:
            return []
        elif len(intervals) == 1:
            return [-1]
        l = len(intervals)
        hash_set = {tuple(intervals[i]): i for i in range(l)}
        intervals = sorted(intervals, key=lambda x: x[0])
        



# print Solution().findRightInterval([[1, 2]]) == [-1]
# print Solution().findRightInterval([[3, 4], [2, 3], [1, 2]]) == [-1, 0, 1]
# print Solution().findRightInterval([[1, 4], [2, 3], [3, 4]]) == [-1, 2, -1]
print Solution().findRightInterval([[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]]) == [3,3,3,4,5,-1]
