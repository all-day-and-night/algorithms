from itertools import combinations
from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
viruses = []
empty = 0
for i in range(N):
    temp = list(map(int, input().split()))
    empty += temp.count(0)
    for j in range(N):
        if temp[j] == 2:
            viruses.append((i, j))

    board.append(temp)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 2500

for cand in combinations(viruses, M):
    lab = deepcopy(board)
    virus = cand

    cnt = 0
    q = deque()
    for v in virus:
        q.append([v[0], v[1], 0])
        lab[v[0]][v[1]] = 1

    infect = empty
    while q:
        #탈출 조건
        if infect == 0:
            break

        x, y, time = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                continue

            if lab[nx][ny] == 0:
                q.append([nx, ny, time + 1])
                infect -= 1
                lab[nx][ny] = 1
                cnt = time + 1

            elif lab[nx][ny] == 2:
                q.append([nx, ny, time + 1])
                lab[nx][ny] = 1
                cnt = time + 1

        if cnt > answer:
            break

    if infect == 0:
        answer = min(answer, cnt)



if answer == 2500:
    print(-1)
else:
    print(answer)

