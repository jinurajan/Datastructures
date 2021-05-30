"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]
"""

from collections import defaultdict


def find_order(tasks, prerequisites):
    sorted_order = []
    graph = defaultdict(list)
    rank = {i: 0 for i in range(tasks)}
    for u, v in prerequisites:
        graph[u].append(v)
        rank[v] += 1

    sources = [k for k, v in rank.items() if v == 0]

    while sources:
        task = sources.pop(0)
        sorted_order.append(task)
        for nei in graph[task]:
            rank[nei] -= 1
            if rank[nei] == 0:
                sources.append(nei)

    return sorted_order


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()

