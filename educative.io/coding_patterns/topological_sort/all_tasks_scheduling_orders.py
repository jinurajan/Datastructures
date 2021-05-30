"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.
"""
from collections import defaultdict


def print_orders(tasks, prerequisites):
    sorted_order = []
    graph = defaultdict(list)
    rank = {i: 0 for i in range(tasks)}
    for u, v in prerequisites:
        graph[u].append(v)
        rank[v] += 1

    sources = [k for k, v in rank.items() if v == 0]
    print_all_topological_order(graph, rank, sources, sorted_order)

def print_all_topological_order(graph, rank, sources, sorted_order):
    if sources:
        for node in sources:
            sorted_order.append(node)
            sources_for_next = sources[:]
            sources_for_next.remove(node)
            for nei in graph[node]:
                rank[nei] -= 1
                if rank[nei] == 0:
                    sources_for_next.append(nei)
            print_all_topological_order(graph, rank, sources_for_next, sorted_order)
            sorted_order.pop()
            for nei in graph[node]:
                rank[nei] += 1
    if len(sorted_order) == len(rank):
        print(sorted_order)

def main():
  print("Task Orders: ")
  print_orders(3, [[0, 1], [1, 2]])

  print("Task Orders: ")
  print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

  print("Task Orders: ")
  print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
