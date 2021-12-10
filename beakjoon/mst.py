import heapq

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(x, parent)
    y = find_parent(y, parent)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y



V, E = map(int, input().split())

edges = []
for i in range(E):
    a, b, e = map(int, input().split())
    heapq.heappush(edges, [e, a-1, b-1])

parent = [i for i in range(V)]

answer = 0
while edges:
    cost, a, b = heapq.heappop(edges)
    if find_parent(a, parent) != find_parent(b, parent):
        union_parent(parent, a, b)
        answer += cost
print(answer)
