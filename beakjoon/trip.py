def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


N = int(input())
M = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

trips = list(map(int, input().split()))

graph = [[] for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if board[i][j] == 1:
            graph[i].append(j)
            graph[j].append(i)

parent = [i for i in range(N)]

for i in range(N):
    for g in graph[i]:
        union(i, g, parent)

prev = parent[trips[0]-1]
isTrue = True
for i in trips:
    if prev != parent[i-1]:
        isTrue = False
        break

if isTrue:
    print("YES")
else:
    print("NO")

