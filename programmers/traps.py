from collections import deque, defaultdict
import heapq
from copy import deepcopy


def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[] for _ in range(n+1)]
    trap_idx = defaultdict(int)
    for trap in traps:
        trap_idx[trap] = 0

    # 0은 정방향, 1은
    INF = int(1e9)
    visited = defaultdict(int)
    for road in roads:
        a, b, cost = road
        graph[a].append([b, cost, 0])
        graph[b].append([a, cost, 1])

    q = []

    heapq.heappush(q, [0, start, trap_idx, 0])

    while q:
        dist, now, trap_, state = heapq.heappop(q)

        if now == end:
            return dist

        for g in graph[now]:
            nxt, cost, state = g
            # now 가 trap일 경우
            # flag가 0이면 정방향
            dir_flag = 0
            temp_trap = deepcopy(trap_)
            next_state = 0
            if now in traps:
                # next 도 trap일 경우
                if nxt in traps:
                    dir_flag = trap_[now] ^ trap_[nxt]
                    temp_trap[nxt] = (temp_trap[nxt] + 1) % 2
                    next_state = 1
                # next는 trap이 아닐경우
                else:
                    dir_flag = trap_[now]

            # now가 trap이 아닐경우
            else:
                # next가 trap일 경우
                if nxt in traps:
                    dir_flag = trap_[nxt]
                    temp_trap[nxt] = (temp_trap[nxt] + 1) % 2
                    next_state = 1
                # next가 trap이 아닐경우
                else:
                    dir_flag = 0
            if dir_flag == state:
                if (now, nxt) in visited:
                    if visited[(now, nxt)] < dist + cost:
                        continue
                visited[(now, nxt)] = dist + cost
                heapq.heappush(q, [dist + cost, nxt, temp_trap, dir_flag])

    return answer

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
solution(n, start, end, roads, traps)