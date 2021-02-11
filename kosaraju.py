import Stack as s

graph = {1: [4, 6],
         2: [7],
         3: [7],
         4: [5],
         5: [1],
         6: [7],
         7: [2, 3]}

graph2 = {1: [5],
          2: [7],
          3: [7],
          4: [1],
          5: [4],
          6: [1],
          7: [2, 3, 6]}


node_num = 7
c = [False] * (node_num + 1)
c2 = [False] * (node_num + 1)
result = []
stack = s.Stack()
stack2 = s.Stack()
scc = []


def dfs(graph, x, c):
    if c[x]:
        return
    c[x] = True
    result.append(x)
    for i in graph[x]:
        dfs(graph, i, c)


def kosaraju(graph, x, c):
    if c[x]:
        return
    c[x] = True
    stack2.push(x)
    for i in graph[x]:
        kosaraju(graph, i, c)


dfs(graph, 1, c)
print(result)

result.reverse()

for i in result:
    stack.push(i)

result.clear()

while stack.is_empty() is False:
    visited = []
    if c2[stack.top()] is False:
        kosaraju(graph2, stack.top(), c2)
        while stack2.is_empty() is False:
            visited.append(stack2.top())
            stack2.pop()
        visited.sort()
        scc.append(visited)
    stack.pop()

scc.sort()

for i in scc:
    print(i)
