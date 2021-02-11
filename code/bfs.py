import Queue as q

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

 
def bfs(graph, start):
    visited = []    # 방문한 노드를 체크하는 리스트
    queue = q.Queue()   # 큐 생성
    queue.enqueue(start)    # 첫 번째 노드 인큐
    while queue.is_empty() is False:    # 큐가 빌 때까지 반복
        for i in graph[queue.peek()]:   # 방문한 노드와 인접한 노드들 인큐
            if i not in visited:        # 방문하지 않은 노드들만 인큐
                queue.enqueue(i)
        visited_node = queue.dequeue()      # 방문한 노드를 저장한 후 디큐
        if visited_node not in visited:     # 방문한 노드를 이미 방문하지 않았을 경우에 방문한 노드에 추가(마지막 구간 예외처리)
            visited.append(visited_node)
    print(visited)


bfs(graph, '1')
# bfs(graph, 'A')
