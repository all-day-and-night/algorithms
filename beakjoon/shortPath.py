import heapq


if __name__ == '__main__':
    INF = int(1e9)

    V, E = map(int, input().split())
    distance = [INF] * (V+1)

    graph = [[] for _ in range(V+1)]

    K = int(input())

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])

    distance[K] = 0

    q = []
    now = K
    heapq.heappush(q, [0, now])

    while q:
        dist, now = heapq.heappop(q)

        for n, cost in graph[now]:
            if distance[n] > dist + cost:
                distance[n] = dist + cost
                heapq.heappush(q, [dist + cost, n])

    for ans in distance[1:]:
        if ans == INF:
            print("INF")

        else:
            print(ans)
