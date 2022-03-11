from heapq import heappush, heappop


def solution(n, edge):
    answer = 0
    INF = int(1e9)

    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    q = []
    heappush(q, [0, 1])
    distance[1] = 0
    while q:
        cnt, now = heappop(q)
        for g in graph[now]:
            if distance[g] > cnt + 1:
                distance[g] = cnt + 1
                heappush(q, [cnt + 1, g])

    return distance.count(max(distance[1:]))


"""import heapq

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n+1)]

    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)


    start = 1
    distance[1] = 0
    q = []
    heapq.heappush(q, [distance[start], start])

    while q:
        dist, now = heapq.heappop(q)
        #print(dist, now, distance[now])

        if dist == INF:
            continue

        for g in graph[now]:
            if distance[g] > dist + 1:
                distance[g] = dist + 1
                heapq.heappush(q, [dist + 1, g])

    distance = distance[1:]
    max_ = max(distance)
    result = len([i for i in distance if i == max_])



    return result"""