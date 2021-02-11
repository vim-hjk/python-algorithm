import math

node_num = 6
# node_num = 4
INF = math.inf

graph = [[0, 2, 5, 1, INF, INF],
         [2, 0, 3, 2, INF, INF],
         [5, 3, 0, 3, 1, 5],
         [1, 2, 3, 0, 1, INF],
         [INF, INF, 1, 1, 0, 2],
         [INF, INF, 5, INF, 2, 0]]

"""
graph = [[0, 5, INF, 8],
         [7, 0, 9, INF],
         [2, INF, 0, 4],
         [INF, INF, 3, 0]]
"""

visited = []
shortest_path = []


def get_smallest_index():
    smallest_distance = INF
    smallest_index = 0
    for i in range(0, node_num):
        if i not in visited and shortest_path[i] < smallest_distance:
            smallest_index = i
    return smallest_index


def dijkstra2(start):
    for i in range(0, node_num):
        shortest_path.append(graph[start][i])
    visited.append(start)
    for _ in range(1, node_num):
        index = get_smallest_index()
        visited.append(index)
        for k in range(0, node_num):
            if shortest_path[k] > shortest_path[index] + graph[index][k]:
                shortest_path[k] = shortest_path[index] + graph[index][k]


dijkstra2(0)
print(shortest_path)
print(visited)