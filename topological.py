# 순서가 있는 작업을 차례대로 정렬해야할 때 쓰는 알고리즘

import Queue as q

graph = {1: [2, 5],
         2: [3],
         3: [4],
         4: [6],
         5: [6],
         6: [7],
         7: []}

node_num = 7    # 노드의 갯수
inDegree = [0] * 8  # 진입차수를 저장할 리스트
inDegree[0] = None
result = []     # 정렬 결과를 저장할 그래프

for i in range(1, node_num + 1):    # 진입차수 계산 및 저장
    for j in graph[i]:
        inDegree[j] += 1


def topological_sort():
    queue = q.Queue()
    for i in range(1, len(inDegree)):   # 진입차수가 0인 노드를 큐에 넣는다(시작점을 큐에 넣는다)
        if inDegree[i] == 0:
            queue.enqueue(i)

    for _ in range(1, node_num + 1):
        if queue.is_empty():    # 큐가 모든 노드를 한 번씩 탐색하기 전에 빈다면 사이클이 있는 그래프이다.
            print("The graph where the cycle exists.")
            break
        visited = queue.peek()  # 방문한 노드
        queue.dequeue()
        result.append(visited)  # 방문한 순서대로 결과 값에 저장
        for k in graph[visited]:   # 노드에 연결된 간선을 제거하고 만약 간선을 제거한 노드의 진입차수가 0이라면 큐에 삽입
            inDegree[k] -= 1
            if inDegree[k] == 0:
                queue.enqueue(k)


topological_sort()
print(result)