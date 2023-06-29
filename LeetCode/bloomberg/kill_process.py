"""
Kill Process

You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, where pid[i] is the ID of the ith process and ppid[i] is the ID of the ith process's parent process.

Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, which means this process has no parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer kill representing the ID of a process you want to kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.


Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]
Explanation: The processes colored in red are the processes that should be killed.
"""
from typing import List


from collections import defaultdict

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent_map = defaultdict(list)
        for child, parent in zip(pid, ppid):
            parent_map[parent].append(child)
        stack = [kill]
        result = []
        while stack:
            parent = stack.pop()
            result.append(parent)
            if parent not in parent_map:
                continue
            for process in parent_map[parent]:
                stack.append(process)
        return result
