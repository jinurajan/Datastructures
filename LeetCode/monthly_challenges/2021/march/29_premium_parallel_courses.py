"""
Parallel Courses

Solution
You are given an integer n which indicates that we have n courses, labeled from 1 to n. You are also given an array relations where relations[i] = [a, b], representing a prerequisite relationship between course a and course b: course a has to be studied before course b.

In one semester, you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses. If there is no way to study all the courses, return -1.



Example 1:


Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
Example 2:


Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they depend on each other.


Constraints:

1 <= n <= 5000
1 <= relations.length <= 5000
1 <= a, b <= n
a != b
All the pairs [a, b] are unique.

"""
from typing import List
from collections import defaultdict


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_count = {i: 0 for i in range(1, n + 1)}
        for start, end in relations:
            graph[start].append(end)
            # inorder to finish end we need to reach from start
            in_count[end] += 1
        print(graph)
        print(in_count)

        q = []
        for node, count in in_count.items():
            if count == 0:
                q.append(node)

        step = 0
        studied_count = 0
        while q:
            step += 1
            next_q = []
            for node in q:
                studied_count += 1
                end_nodes = graph[node]
                for end_node in end_nodes:
                    in_count[end_node] -= 1
                    if in_count[end_node] == 0:
                        next_q.append(end_node)
            q = next_q
        return step if studied_count == n else -1




