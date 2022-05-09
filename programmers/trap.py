import heapq
from collections import defaultdict

n = 3
start = 1
end = 1
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]



def solution(n, start, end, roads, traps):
    graph = make_graph(n, roads)
    #traps의 부분이 비트마스킹의 가장 중요한 부분
    traps = {traps[i]: i for i in range(len(traps))}
    dist = solve(start, graph, traps)
    print(dist[end])
    return min(dist[end])

def make_graph(n, roads):
    graph = [defaultdict(lambda: 3001) for _ in range(n+1)]
    for P, Q, S in roads:
        graph[P][Q] = min(graph[P][Q], S)
        graph[Q][-P] = min(graph[Q][-P], S)

    return graph


def solve(start, graph, traps):
    INF = int(1e9)
    dist = [[INF] * (2**10) for _ in range(len(graph))]
    print(len(dist))
    print(len(dist[0]))
    dist[start][0] = 0
    q = [[0, start, 0]]

    while q:
        now_dist, now_node, now_status = heapq.heappop(q)

        for adj, adj_dist in graph[now_node].items():
            direction = True if adj > 0 else False
            adj = abs(adj)

            adj_trapped = 0 if adj not in traps.keys() else ((now_status & (1 << traps[adj])) != 0)
            now_trapped = 0 if now_node not in traps.keys() else ((now_status & (1 << traps[now_node])) != 0)

            #True 정방향, False 역방향
            edge_reversed = (adj_trapped == now_trapped)

            #방향이 일치할 경우
            if direction != edge_reversed:
                next_status = now_status

                #trap일경우 status 변경
                if adj in traps.keys():
                    next_status = now_status ^ (1 << traps[adj])

                new_dist = now_dist + adj_dist
                #비트마스킹의 결과는 traps의 모든 형태릂 보여줌. 그러니까 배열의 크기를 2 ** 10 으로 잡은 거임
                if dist[adj][next_status] > new_dist:
                    dist[adj][next_status] = new_dist
                    heapq.heappush(q, [new_dist, adj, next_status])
    return dist





print(solution(n, start, end, roads, traps))