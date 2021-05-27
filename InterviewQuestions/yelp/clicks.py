import random

ORIGINAL_CLICKS = [
    ("Home", "Home Cleaning"),
    ("Home", "Restaurants"),
    ("Restaurants", "Delivery"),
    ("Delivery", "Address Search"),
    ("Address Search", "Burgers"),
    ("Burgers", "Order Delivery"),
    ("Order Delivery", "Start Order"),
    ("Start Order", "Turkey Burger"),
    ("A", "B"),
    ("B", "C")
]

# Oh darn, now they're all mixed up!
CLICKS = ORIGINAL_CLICKS[:]
random.shuffle(CLICKS)

# Given the shuffled click data and an origin page, find the final destination page
# ex: input: 'Home' -> output: 'Turkey Burger'


#######   YOUR SOLUTION HERE   ############

# {home: [home cleaning], 'home cleaning: [restaurants], ...}  # representation

from collections import defaultdict
def find_path(origin):
    graph = defaultdict(list)
    for each in CLICKS:
        graph[each[0]].append(each[1])
    stack = [origin]
    visited = set()
    result = []
    while stack:
        node = stack.pop()
        if node in visited:
            raise Exception("Invalid Input")
        visited.add(node)
        if node not in graph:
            result.append(node)
        for nei in graph[node]:
            stack.append(nei)

    return result


print(find_path("Delivery"))
# print(find_path("Home"))
# print(find_path("A"))





