import Union_Find as uf


# 간선 클래스
class Edge:
    def __init__(self, distance, node1, node2):
        self.distance = distance    # 비용
        self.node1 = node1  # 연결된 노드1
        self.node2 = node2  # 연결된 노드2


# 노드의 갯수
num_node = 7

# 간선 집합
edge = [Edge(12, 1, 7), Edge(28, 1, 4), Edge(67, 1, 2), Edge(17, 1, 5),
        Edge(24, 2, 4), Edge(62, 2, 5),
        Edge(20, 3, 5), Edge(37, 3, 6),
        Edge(13, 4, 7),
        Edge(45, 5, 6), Edge(73, 5, 7)]


# 퀵 정렬로 비용이 작은 순서대로 간선 정렬
def edge_sort(start, end):
    if start >= end:
        return
    pivot = start
    left_idx = start + 1
    right_idx = end
    while left_idx <= right_idx:
        while left_idx <= end and edge[left_idx].distance < edge[pivot].distance:
            left_idx += 1
        while right_idx > start and edge[right_idx].distance > edge[pivot].distance:
            right_idx -= 1
        if left_idx > right_idx:
            edge[right_idx], edge[pivot] = edge[pivot], edge[right_idx]
        else:
            edge[left_idx], edge[right_idx] = edge[right_idx], edge[left_idx]

    edge_sort(start, right_idx - 1)
    edge_sort(right_idx + 1, end)


# 간선을 정렬
edge_sort(0, 10)

# 사이클이 있는지 검사할 리스트
check_cycle = [None] * (num_node + 1)

# 각 노드가 포함된 그래프가 어디인지 저장
for i in range(1, num_node + 1):
    check_cycle[i] = i

sum = 0     # 최소비용 신장트리 간선비용의 합을 저장할 변수
line = []   # 비용들을 저장할 리스트

for i in edge:
    # 동일한 부모노드를 가리키지 않을경우(사이클이 발생하지 않을 경우만 선택)
    # 간선을 비용이 낮은 순서대로 정렬한 상태이므로, 사이클이 발생할 수 있는 간선은 이미 부모노드가 같을 것이므로 계산하지 않는다.
    if uf.findParent(check_cycle, i.node1, i.node2) is False:
        sum += i.distance
        line.append(i)
        uf.unionParent(check_cycle, i.node1, i.node2)

for j in line:
    print(j.distance, "/", j.node1, "/", j.node2)

print(sum)
