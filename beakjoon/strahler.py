from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

inputs = []
for loop in range(N):
    K, M, P = map(int, input().split())

    graph = [[] for _ in range(M+1)]
    parents = [[] for _ in range(M+1)]
    orders = [0] * (M+1)
    indegree = [0] * (M+1)

    firsts = set([i for i in range(1, M+1)])
    for _ in range(P):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
        firsts.discard(b)

    firsts = list(firsts)

    q = deque()

    for i in range(1, M+1):
        if indegree[i] == 0:
            q.append(i)
            orders[i] = 1

    answer = -1

    while q:
        now = q.popleft()
        answer = max(answer, orders[now])

        for b in graph[now]:
            indegree[b] -= 1
            parents[b].append(orders[now])

            if indegree[b] == 0:
                i = max(parents[b])
                cnt = parents[b].count(i)
                if cnt > 1:
                    orders[b] = i + 1
                elif cnt == 1:
                    orders[b] = i

                q.append(b)
    print(loop+1, answer)
