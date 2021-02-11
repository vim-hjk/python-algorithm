parent = [None] * 11


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    parent[b] = a


for i in range(1, 11):
    parent[i] = i

union(1, 2)
union(2, 3)
union(3, 4)
union(5, 6)
union(6, 7)
union(7, 8)

print(parent)