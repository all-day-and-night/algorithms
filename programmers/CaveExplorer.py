from collections import deque


def solution(n, path, order):
    answer = True

    orders = {}
    for a, b in order:
        orders[b] = a

    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]

    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    wait = {}

    q = deque()
    q.append(0)
    num = 0
    while q:
        now = q.pop()

        if now in orders.keys() and not visited[orders[now]]:
            wait[orders[now]] = now
            continue

        visited[now] = True
        num += 1

        for g in graph[now]:
            if visited[g] == False:
                q.append(g)

        if now in wait.keys():
            q.append(wait[now])

    if num == n:
        return True
    else:
        return False


