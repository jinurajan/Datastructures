"""
uses adjascency matrix for calculating the shortest path in a single run / visit of all nodes

1. select an intermediate array and connect all it's edges by adding the sum and update the matrix on the go

"""


def shortest_path(start, end, edges):
    distance = [[ 0 if i == j else float("inf") for i in range(5)] for j in range(5)]
    for u, v, w in edges:
        distance[u-1][v-1] = w
        distance[v-1][u-1] = w
    for i in range(5):
        for j in range(5):
            for k in range(5):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    return distance[start-1][end-1]

edges = [[3, 2, 2], [3, 4, 6], [2, 1, 5], [1, 5, 1], [5, 4, 2], [1, 4, 9]]

print(shortest_path(1, 4, edges))