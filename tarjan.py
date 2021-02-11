import Stack as s

graph = {1: [2],
         2: [3],
         3: [1],
         4: [2, 5],
         5: [7],
         6: [5],
         7: [6],
         8: [5, 9],
         9: [10],
         10: [11],
         11: [3, 8]}

node_num = 11

stack = s.Stack()
visited = [None] * (node_num + 1)
finished = [False] * (node_num + 1)
result = []


def tarjan(node):
    visited[node] = node
    stack.push(node)
    parent = visited[node]
    for j in graph[node]:
        if visited[j] is None:
            parent = min(parent, tarjan(j))
        elif finished[j] is False:
            parent = min(parent, visited[j])

    if parent == visited[node]:
        scc = []
        while True:
            top = stack.top()
            stack.pop()
            scc.append(top)
            finished[top] = True
            if top == node:
                break
        result.append(scc)

    return parent


for i in range(1, node_num + 1):
    if visited[i] is None:
        tarjan(i)
print(result)


