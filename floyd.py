import math
import copy

node_num = 4
INF = math.inf
graph = [[0, 5, INF, 8],
         [7, 0, 9, INF],
         [2, INF, 0, 4],
         [INF, INF, 3, 0]]

shortest_path = copy.deepcopy(graph)


def floyd_warshall():
    for k in range(0, node_num):
        for i in range(0, node_num):
            for j in range(0, node_num):
                if shortest_path[i][j] > shortest_path[i][k] + shortest_path[k][j]:
                    shortest_path[i][j] = shortest_path[i][k] + shortest_path[k][j]


floyd_warshall()
print(shortest_path)
