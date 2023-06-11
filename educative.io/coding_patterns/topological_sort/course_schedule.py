"""
There are a total of num_courses courses you have to take. The courses are labeled from 0 to num_courses - 1. You are also given a prerequisites array, where prerequisites[i] = [a[i], b[i]] indicates that you must take course b[i] first if you want to take the course a[i]. 
For example, the pair [1,0] indicates that to take course 1 you have to first take course 0
Return TRUE if all of the courses can be finished. Otherwise, return FALSE.

"""



from collections import deque
from collections import Counter
from collections import defaultdict


def can_finish(num_courses, prerequisites):
    adj_list = defaultdict(list)
    indegrees = {i: 0 for i in range(num_courses)}

    for a, b in prerequisites:
        adj_list[b].append(a)
        indegrees[a] += 1
    
    sources = deque([k for k,v in indegrees.items() if v == 0])
    sorted_order = []
    while sources:
        sub = sources.popleft()
        sorted_order.append(sub)
        for dep in adj_list[sub]:
            indegrees[dep] -= 1
            if indegrees[dep] == 0:
                sources.append(dep)
        
    if len(sorted_order) == num_courses:
        return True
    # Write your code here

    return False
