"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2]


"""
from collections import defaultdict
def is_scheduling_possible(tasks, prerequisites):
      graph = defaultdict(list)
      rank = {i: 0 for i in range(tasks)}
      for u, v in prerequisites:
            graph[u].append(v)
            rank[v] += 1
      sources = [k for k, v in rank.items() if v == 0]
      visited = set()
      while sources:
            course = sources.pop(0)
            visited.add(course)
            for nei in graph[course]:
                  rank[nei] -= 1
                  sources.append(nei)
      return len(visited) == tasks



def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()
