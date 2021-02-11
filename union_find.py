node_num = 8


# 연결된 노드 중 부모노드를 찾아서 반환
def getParent(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getParent(parent, parent[x])
        return parent[x]


# 노드 연결하기, 더 작은 노드를 부모노드로 한다.
def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 연결여부 확인
def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return True
    else:
        return False


parent = [None] * (node_num + 1)
for i in range(1, node_num + 1):
    parent[i] = i
unionParent(parent, 1, 2)
unionParent(parent, 2, 3)
unionParent(parent, 3, 4)
unionParent(parent, 5, 6)
unionParent(parent, 6, 7)
unionParent(parent, 7, 8)



print(parent)