"""
Let’s assume that there are a total of n courses labeled from  0 to n-1. Some courses may have prerequisites. A list of prerequisites is specified such that if 
prerequisities=a,b , you must take course b before course  a

Given the total number of courses n and a list of the prerequisite pairs, return the course order a student should take to finish all of the courses. If there are multiple valid orderings of courses, then the return any one of them.

Note: There can be a course in the  0 to n-1 range with no prerequisites.
"""

from collections import defaultdict
from collections import Counter

def find_order(n, prerequisites):
    graph = defaultdict(list)
    indegrees = {i: 0 for i in range(n)}

    for a, b in prerequisites:
        graph[b].append(a)
        indegrees[a] += 1
    
    sources =[k for k,v in indegrees.items() if v == 0]

    sorted_order = []
    while sources:
        # queue hence pop(0)
        subject = sources.pop(0)
        sorted_order.append(subject)
        for prereq in graph[subject]:
            indegrees[prereq] -= 1
            if indegrees[prereq] == 0:
                sources.append(prereq)
    if len(sorted_order) != n:
        return []
    return sorted_order