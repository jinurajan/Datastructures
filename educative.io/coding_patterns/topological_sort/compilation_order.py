"""
There are a total of n classes labeled with the English alphabet (A,B,C and so on). Some classes are dependent on other classes for compilation. For example, if class 
B extends class A, then  B has a dependency on A. Therefore, Amust be compiled before B
Given a list of the dependency pairs, find the order in which the classes should be compiled
"""

from collections import deque
from collections import defaultdict
from collections import Counter

# Tip: You may use some of the code templates provided
# in the support file

def find_compilation_order(dependencies):
  adj_list = defaultdict(list)
  indegree = Counter()
  for u, v in dependencies:
    indegree[u] = 0
    indegree[v] = 0
  for u, v in dependencies:
    adj_list[v].append(u)
    indegree[u] += 1
  
  q = deque([node for node,val in indegree.items() if val == 0])
  sorted_order = []
  while q:
    node = q.popleft()
    sorted_order.append(node)
    for neigh in adj_list[node]:
      indegree[neigh] -= 1
      if indegree[neigh] == 0:
        q.append(neigh)
  return sorted_order
