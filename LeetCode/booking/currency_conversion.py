"""
Paramenters:

array of currency conversion rates. E.g. ['USD', 'GBP', 0.77] which means 1 USD is equal to 0.77 GBP
an array containing a 'from' currency and a 'to' currency
Given the above parameters, find the conversion rate that maps to the 'from' currency to the 'to' currency.
Your return value should be a number.

Example:
You are given the following parameters:

Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
To/From currency ['GBP', 'AUD']
Find the rate for the 'To/From' curency. In this case, the correct result is 1.89.

1. create a graph from the rates with to and from rates
2. find path from A to B
"""
from collections import defaultdict
from collections import deque

def find_exchange_rate(rates, start, end):
    graph = defaultdict(dict)

    for u, v, value in rates:
        graph[u][v] = value
        graph[v][u] = 1.0 / value
    visited = set()
    # BFS
    queue = deque()
    queue.append((start, 1.0))

    while queue:
        curr, num = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)
        if curr in graph:
            neighbour = graph[curr]
            for next_curr, val in neighbour.items():
                if next_curr not in visited:
                    if next_curr == end:
                        return num* val
                    queue.append((next_curr, num * val))
        
    return -1

from heapq import heappop, heappush

def find_exchange_rate_1(rates, start, end):
    graph = defaultdict(dict)

    for u, v, value in rates:
        graph[u][v] = value
        graph[v][u] = 1.0 / value

    #dijkstras algorithm
    distance = {curr: float("inf") for curr in graph}
    if end not in distance:
        return -1
    distance[start] = 1
    visited = set()
    min_heap = [(1, start)]
    while min_heap:
        val, curr = heappop(min_heap)
        if curr in visited:
            continue
        visited.add(curr)
        for new_curr, new_val in graph[curr].items():
            new_rate = val * new_val
            if new_rate < distance[new_curr]:
                distance[new_curr] = new_rate
                heappush(min_heap, (new_rate, new_curr))
    
    
    return -1 if distance[end] == float("inf") else distance[end]


data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070)]

print(find_exchange_rate(data, 'GBP', 'AUD'))
print(find_exchange_rate(data, 'GBP', 'XYZ'))
print(find_exchange_rate(data, 'JPY', 'AUD'))
print(find_exchange_rate_1(data, 'GBP', 'AUD'))
print(find_exchange_rate_1(data, 'GBP', 'XYZ'))
print(find_exchange_rate_1(data, 'JPY', 'AUD'))




