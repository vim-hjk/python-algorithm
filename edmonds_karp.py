import Queue as q
import math

# 노드의 갯수
num_node = 6

# 간선 집합
graph = {1: [2, 4],
         2: [1, 3, 4, 5, 6],
         3: [2, 5, 6],
         4: [1, 2, 5],
         5: [2, 3, 4, 6],
         6: [2, 3, 5]}

flow = [[0] * (num_node + 1) for i in range(num_node + 1)]
capacity = [[0] * (num_node + 1) for j in range(num_node + 1)]

capacity[1][2] = 12
capacity[1][4] = 11
capacity[2][3] = 6
capacity[2][4] = 3
capacity[2][5] = 5
capacity[2][6] = 9
capacity[3][6] = 8
capacity[4][5] = 9
capacity[5][3] = 3
capacity[5][6] = 4
d = []
result = 0


def edmonds_karp(start, end):
    global result
    global d
    while True:
        d = [-1] * (num_node + 1)
        queue = q.Queue()
        queue.enqueue(start)
        while queue.is_empty() is False:
            x = queue.peek()
            queue.dequeue()
            for i in graph[x]:
                if capacity[x][i] - flow[x][i] > 0 and d[i] == -1:
                    queue.enqueue(i)
                    d[i] = x
                    if i == end:
                        break
        print("d[end]", d[end])
        if d[end] == -1:
            break
        f = math.inf
        idx = end
        while idx != start:
            f = min(f, capacity[d[idx]][idx] - flow[d[idx]][idx])
            idx = d[idx]
        idx = end
        while idx != start:
            flow[d[idx]][idx] += f
            flow[idx][d[idx]] -= f
            idx = d[idx]
        result += f


edmonds_karp(1, 6)
print(result)
for i in range(1, 7, 1):
    for j in range(1, 7, 1):
        if flow[i][j] > 0:
            print("flow[", i, "][", j, "] = ", flow[i][j])




