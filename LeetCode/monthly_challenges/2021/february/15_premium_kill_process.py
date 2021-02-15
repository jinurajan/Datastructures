"""
Kill Process

Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

Input:
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation:
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.

Note:
The given kill id is guaranteed to be one of the given PIDs.
n >= 1.
"""
from typing import List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent_process_map = {}
        for idx in range(len(ppid)):
            if ppid[idx] not in parent_process_map:
                parent_process_map[ppid[idx]] = [pid[idx]]
            else:
                parent_process_map[ppid[idx]].append(pid[idx])

        q = [kill]
        res = []
        while q:
            parent_proc = q.pop()
            res.append(parent_proc)
            if parent_proc not in parent_process_map:
                continue
            for process in parent_process_map[parent_proc]:
                q.append(process)
        return res

pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
print(Solution().killProcess(pid, ppid, kill))
