import Stack as s

graph = {'1': ['2', '3'],
         '2': ['1', '3', '4', '5'],
         '3': ['1', '2', '6', '7'],
         '4': ['2', '5'],
         '5': ['2', '4'],
         '6': ['3', '7'],
         '7': ['3', '6']}

"""
graph = {'A': ['B', 'C'],
         'B': ['A', 'D'],
         'C': ['A', 'E', 'F'],
         'D': ['B', 'E'],
         'E': ['C', 'D'],
         'F': ['C', 'G'],
         'G': ['F']}
"""

stack = s.Stack()
result = []
visited = []


def dfs(graph, node):
    if node in visited:
        return
    visited.append(node)
    result.append(node)
    for i in graph[node]:
        dfs(graph, i)


dfs(graph, '1')
# dfs(graph, 'A')
print(result)
