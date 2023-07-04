"""
Minimize the Total Price of the Trips

There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Each node has an associated price. You are given an integer array price, where price[i] is the price of the ith node.

The price sum of a given path is the sum of the prices of all nodes lying on that path.

Additionally, you are given a 2D integer array trips, where trips[i] = [starti, endi] indicates that you start the ith trip from the node starti and travel to the node endi by any path you like.

Before performing your first trip, you can choose some non-adjacent nodes and halve the prices.

Return the minimum total price sum to perform all the given trips.


Input: n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]
Output: 23

"""
from typing import List
from functools import lru_cache


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        s = 0
        used_node_count = {}
        for from_trip, to_trip in trips:
            path, trip_price = self.find_shortest_path(adj_list, price, from_trip, to_trip)
            s += trip_price
            for node in path:
                used_node_count[node] = used_node_count.get(node, 0) + 1
        
        cache = {}
        mx1 = self.find_min_price(None, 0, True, adj_list, used_node_count, price, cache)
        mx2 = self.find_min_price(None, 0, False, adj_list, used_node_count, price, cache)
        return min(mx1, mx2)
    
    def find_min_price(self, parent, node, selected, adj_list, used_node_count, price, cache):
        if(node, selected) in cache:
            return cache[(node, selected)]
        if selected:
            cost = (price[node] // 2) * used_node_count.get(node, 0)
        else:
            cost = price[node] * used_node_count.get(node, 0)
        
        mins = []
        for child in adj_list[node]:
            if child == parent:
                continue
            options = []
            if not selected:
                mx = self.find_min_price(node, child, True, adj_list, used_node_count, price, cache)
                options.append(mx)
            mx = self.find_min_price(node, child, False, adj_list, used_node_count, price, cache)
            options.append(mx)
            mins.append(min(options))
        
        cache[(node, selected)] = cost + sum(mins)
        return cost + sum(mins)



    def find_shortest_path(self, adj_list:List, price:int, from_trip, to_trip):
        dist = [float("inf")] * (len(adj_list))

        parents = {}
        dist[from_trip] = price[from_trip]
        visited = set()
        stack = [from_trip]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for neigh in adj_list[node]:
                curr_dist = dist[node] + price[neigh]
                if dist[neigh] < curr_dist:
                    continue
                dist[neigh] = curr_dist
                parents[neigh] = node
                stack.append(neigh)
                if neigh in visited:
                    visited.remove(node)
        path = [to_trip]
        curr_node = to_trip
        while curr_node != from_trip:
            curr_node = parents[curr_node]
            path.append(curr_node)
        
        return path, dist[to_trip]





from collections import Counter, defaultdict
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
       
        count = Counter()
    
        totalCost = 0

        def dfs(node,par,end):
            nonlocal count
            nonlocal totalCost
            if node == end:
                return True
            
            for nei in graph[node]:
                if nei != par:
                    if dfs(nei, node, end):
                        count[nei] += 1
                        totalCost += price[nei]
                        return True
            return False

       
        for start,end in trips:
            count[start] += 1
            totalCost += price[start]
            dfs(start,None,end)
        
      
        @lru_cache
        def dp(node, par, canReduce):
            if canReduce:
                res = (price[node]//2)*count[node]
            else:
                res = 0
            red = 0
            for nei in graph[node]:
                if nei != par:
               
                    if canReduce:
                        cur = dp(nei, node, False)

                    else:
                        cur = max(dp(nei, node, False), dp(nei, node, True))
                    red += cur
            return res + red
        
    
        reduce = 0
        for i in range(n):
            reduce = max( reduce, dp(i, None, True), dp(i, None, False) )
        
    
        return totalCost - reduce



from collections import defaultdict
from collections import Counter
import heapq

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        n = len(edges)+ 1
        graph = {i: [] for i in range(n+1)}
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # find all actual path values with a map of number of visits on nodes in the path for each trips
        sum_val = 0
        counter = Counter()
        for start, end in trips:
            path, route_price = self.find_shortest_path(graph, start, end, price)
            sum_val += route_price
            for node in path:
                counter[node] += 1
        cache = {}
        mx1 = self.find_min_price(None, 0, True, graph, counter, price, cache)
        mx2 = self.find_min_price(None, 0, False, graph, counter, price, cache)
        return min(mx1, mx2)
    
    def find_min_price(self, parent, node, selected, graph, counter, price, cache):
        if (node, selected) in cache:
            return cache[(node, selected)]
        if selected:
            cost = (price[node]//2) * counter[node]
        else:
            cost = price[node] * counter[node]
        
        mins = []
        for neighbour in graph[node]:
            if neighbour == parent:
                continue
            options = []
            if not selected:
                mx = self.find_min_price(node, neighbour, True, graph, counter, price, cache)
                options.append(mx)
            mx = self.find_min_price(node, neighbour, False, graph, counter, price, cache)
            options.append(mx)
            mins.append(min(options))
        cache[(node, selected)] = cost + sum(mins)
        return cost + sum(mins)
        

    
    def find_shortest_path(self, graph, start, end, price):
        parents = {}
        distance = [float("inf") for _ in range(len(graph))]
        distance[start] = price[start]
        visited = set()
        min_heap = [(0, start)]
        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            for nei in graph[node]:
                new_dist = distance[node] + price[nei]
                if new_dist < distance[nei]:
                    distance[nei] = new_dist
                    parents[nei] = node
                    heapq.heappush(min_heap, (new_dist, nei))
        path = [end]
        curr_node = end
        while curr_node != start:
            curr_node = parents[curr_node]
            path.append(curr_node)
        return path, distance[end]