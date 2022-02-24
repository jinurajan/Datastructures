"""
Find 4 countries directly connected which can get max money?
Given list of countries & money located -

UK, 10
Spain, 20
USA, 19
Germany, 7
Ireland, 11
UAE, 9
N countries
Countries connected
Germany - USA
USA - UK
Germany - Spain
UAE - Ireland
Ireland - UK
M connection


Return max money can be collected for 4 countries.

How do you solve this?
"""
from collections import defaultdict
import heapq

def max_money_for_four_countries(country_map, connections):
    result = 0
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    for country, money in country_map.items():
        max_countries = 4
        current_max = 0
        pq = []
        visited = set()
        heapq.heappush(pq, (money, country))
        while pq and max_countries > 0:
            curr_money, curr_country = heapq.heappop(pq)
            current_max += curr_money
            for neighbour in graph[curr_country]:   
                if neighbour not in visited:
                    visited.add(neighbour)
                    heapq.heappush(pq, (country_map[neighbour], neighbour))
            max_countries -= 1

        if not max_countries:
            result = max(result, current_max)    

    return result


country_map = {
    "UK": 10,
    "Spain": 20,
    "USA": 19,
    "Germany": 7,
    "Ireland": 11,
    "UAE": 9
}

connections = [
    ("Germany", "USA"),
    ("USA", "UK"),
    ("Germany", "Spain"),
    ("UAE", "Ireland"),
    ("Ireland", "UK")
]

print(max_money_for_four_countries(
    country_map=country_map,
    connections=connections
))