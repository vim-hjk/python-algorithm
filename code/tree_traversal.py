# 노드 구조
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


# 순회 결과를 저장할 리스트
pre_result = []
in_result = []
post_result = []


# 전위 순회
def pre_order(start):
    if start:
        pre_result.append(start.data)
        pre_order(start.left_child)
        pre_order(start.right_child)


# 중위순회
def in_order(start):
    if start:
        in_order(start.left_child)
        in_result.append(start.data)
        in_order(start.right_child)


# 후위 순회
def post_order(start):
    if start:
        post_order(start.left_child)
        post_order(start.right_child)
        post_result.append(start.data)


# 노드의 갯수
number = 15

# 노드를 저장할 리스트
nodes = [None] * (number + 1)

# 노드 초기화
for i in range(1, number + 1):
    nodes[i] = Node(i)

# 노드에 자식 노드 연결
for i in range(2, number + 1):
    if i % 2 == 0:
        nodes[i // 2].left_child = nodes[i]
    else:
        nodes[i // 2].right_child = nodes[i]


pre_order(nodes[1])
in_order(nodes[1])
post_order(nodes[1])

print("전위 순회 :", pre_result)
print("중위 순회 :", in_result)
print("후위 순회 :", post_result)