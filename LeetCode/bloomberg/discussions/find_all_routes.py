"""
Given one directional airport connections, devise a solution that can provide the route from Airport A to Airport B.

Implement 2 functions: one that adds a one-directional airport connection between 2 airports, and second that return out all possible routes between an origin and a destination. This could be done by implementing a class called AirMap that has two methods:


"""
from collections import defaultdict

class AirMap():
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_connection(self, start, destination):
        self.graph[start].append(destination)
    

    def backtrack(self,current, destination, current_route, routes, visited):
        visited.add(current)
        current_route.append(current)
        if current == destination:
            routes.append(current_route[:])
        else:
            for neigh_airport in self.graph[current]:
                if neigh_airport not in visited:
                    self.backtrack(neigh_airport, destination, current_route, routes, visited)
        
        visited.remove(current)
        current_route.pop()

    def get_all_routes(self, start, destination):
        routes = []
        self.backtrack(start, destination, [], routes, set())
        return routes




air_map = AirMap()
air_map.add_connection('A', 'B')
air_map.add_connection('B', 'A')
air_map.add_connection('A', 'C')
air_map.add_connection('C', 'A')
air_map.add_connection('A', 'D')
air_map.add_connection('D', 'A')
air_map.add_connection('B', 'C')
air_map.add_connection('C', 'B')
air_map.add_connection('B', 'D')
air_map.add_connection('D', 'B')


print(air_map.get_all_routes('C', 'D'))



