"""
bfs로 풀었는데 메모리초과 때문에 개고생한듯
다른 풀이를 보니 bfs를 사용하지 않고 그냥 앞 뒤만 고려해서 푼 것을 보고 풀어보니 해결됨
앞뒤가 이어지는 것은 deque의 rotate를 쓰자
"""

import sys
from collections import deque


input = sys.stdin.readline


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, T = map(int, input().split())

plates = []
result = 0
for i in range(N):
    plates.append(deque(list(map(int, input().split()))))
    result += sum(plates[i])

info = []
for _ in range(T):
    info.append(list(map(int, input().split())))


for x, d, k in info:
    if result == 0:
        break

    dir_ = 0
    if d == 0:
        dir_ = 1
    else:
        dir_ = -1

    result = 0
    for i in range(N):
        result += sum(plates[i])
        if (i + 1) % x == 0:
            plates[i].rotate(k * dir_)

    if result == 0:
        break

    check = False
    remove = set()
    for i in range(N):
        for j in range(M):
            if plates[i][j] != 0 and plates[i][j] == plates[i][(j+1) % M]:
                remove.add((i, j))
                remove.add((i, (j+1) % M))

    for i in range(N-1):
        for j in range(M):
            if plates[i][j] != 0 and plates[i][j] == plates[i+1][j]:
                remove.add((i, j))
                remove.add((i+1, j))

    if len(remove) < 1:
        sum_ = 0
        cnt = 0
        for p in plates:
            sum_ += sum(p)
            cnt += M - p.count(0)

        average = sum_ / cnt
        for i in range(N):
            for j in range(M):
                if plates[i][j] != 0:
                    if plates[i][j] > average:
                        plates[i][j] -= 1
                    elif plates[i][j] < average:
                        plates[i][j] += 1

    else:
        while remove:
            x, y = remove.pop()
            plates[x][y] = 0



result = 0
for p in plates:
    result += sum(p)

print(result)


