import Priority_Queue as pq
import math


# 간선 클래스
class Edge:
    def __init__(self, distance, node):
        self.distance = distance    # 비용
        self.node = node  # 연결된 노드


INF = math.inf  # 연결되어 있지 않은 노드 간의 거리

node_num = 6    # 노드의 갯수

graph = [[None],
         [None, Edge(2, 2), Edge(5, 3), Edge(1, 4)],
         [None, Edge(2, 1), Edge(3, 3), Edge(2, 4)],
         [None, Edge(5, 1), Edge(3, 2), Edge(3, 4), Edge(1, 5), Edge(5, 6)],
         [None, Edge(1, 1), Edge(2, 2), Edge(3, 3), Edge(1, 5)],
         [None, Edge(1, 3), Edge(1, 4), Edge(2, 6)],
         [None, Edge(5, 3), Edge(2, 5)]]

shortest_path = [INF] * (node_num + 1)  # 최단경로의 비용을 저장할 리스트


def dijkstra(start):
    p_queue = pq.Priority_Queue()   # 우선순위 큐 생성
    shortest_path[start] = 0    # 출발지에서 출발지로 가는 비용을 0으로 설정
    p_queue.enqueue((0, start)) # 우선순위 큐에 인큐
    while p_queue.is_empty() is False:  # 큐가 빌 때까지 반복
        distance, current = p_queue.dequeue()   # 디큐하여 비용과 현재 노드값을 저장
        if shortest_path[current] < distance:   # 최단 거리가 아닌 경우 스킵
            continue
        for j in range(1, len(graph[current])): # 현재 노드의 간선 수 만큼 반복
            next = graph[current][j].node   # 인접 노드
            next_distance = distance + graph[current][j].distance # 출발지점에서 인접노드로 가는 비용과 인접 노드에서 도착지점으로 가는 비용을 더한 값
            if next_distance < shortest_path[next]:  # 거쳐가는 것이 더 작다면
                shortest_path[next] = next_distance  # 최단 경로를 갱신
                p_queue.enqueue((next_distance, next))  # 비용과 노드를 인큐


dijkstra(1)

print(shortest_path[1:])
