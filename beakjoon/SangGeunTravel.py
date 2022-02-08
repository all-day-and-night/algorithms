import sys

input = sys.stdin.readline


def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a == b:
        return

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())
answer = []
for _ in range(T):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    INF = int(1e9)
    parent = [i for i in range(N+1)]

    cnt = 0
    for i in range(1, N):
        for j in range(i+1, N+1):
            if parent[i] != parent[j]:
                union(i, j, parent)
                cnt += 1

    answer.append(cnt)

for ans in answer:
    print(ans)
