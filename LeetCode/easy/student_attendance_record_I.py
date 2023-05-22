"""
Student Attendance Record I

You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

"""

class Solution1:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        for idx, char in enumerate(s):
            if char == 'A':
                a_count += 1
            if idx <= len(s) -3 and s[idx] == 'L' and s[idx+1] == 'L' and s[idx+2] == 'L':
                return False
        return a_count < 2

class Solution2:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        for idx, char in enumerate(s):
            if char == 'A':
                a_count += 1
        
        return a_count < 2 and 'LLL' not in s
        
class Solution:
    def checkRecord(self, s: str) -> bool:
        # number of 'A' < 2
        # number of consecutive 'L' < 3
        def max_consecutive_ls(s, lower, upper):
            max_ls = 0
            count = 0
            start = lower
            end = lower
            while end <= upper:
                if s[end] == 'L':
                    if start is None:
                        start = end
                    end += 1
                    count += 1
                    continue
                else:
                    max_ls = max(count, max_ls)
                    end += 1
                    start = None
                    count = 0
            max_ls = max(count, max_ls)
            return max_ls
        a_count = 0
        start_l_index = None
        end_l_index = None
        for idx, char in enumerate(s):
            if char == 'A':
                a_count += 1
            if char == 'L':
                if start_l_index == None:
                    start_l_index = idx
                end_l_index = idx
        if start_l_index is None and end_l_index is None:
            max_ls = 0
        else:
            max_ls = max_consecutive_ls(s, start_l_index, end_l_index)
        
        return a_count < 2 and max_ls < 3
        
        