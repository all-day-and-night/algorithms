def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a != b:
        parent[a] = b


N, M = map(int, input().split())

parent = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    if find(a, parent) != find(b, parent):
        union(a, b, parent)

for i in range(1, N+1):
    find(i, parent)

print(len(set(parent[1:])))




