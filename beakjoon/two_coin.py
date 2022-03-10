from collections import deque
import heapq

N, M = map(int, input().split())

board = []

coins = []
for i in range(N):
    temp = list(input())
    for j in range(M):
        if temp[j] == 'o':
            coins.append([i, j])
    board.append(temp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def getRange(x, y):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return False
    return True


dicts = {}
dicts[(coins[0][0], coins[0][1], coins[1][0], coins[1][1])] = 0


def bfs(x1, y1, x2, y2):
    q = deque()
    q.append([0, x1, y1, x2, y2])

    while q:
        cnt, x1, y1, x2, y2 = q.popleft()
        if cnt > 9:
            return -1

        for i in range(4):
            nx1, ny1 = x1 + dx[i], y1 + dy[i]
            nx2, ny2 = x2 + dx[i], y2 + dy[i]

            flag1 = getRange(nx1, ny1)
            flag2 = getRange(nx2, ny2)

            if flag1 and flag2:
                if board[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                if nx1 == nx2 and ny1 == ny2:
                    continue
                if (nx1, ny1, nx2, ny2) in dicts.keys():
                    if dicts[(nx1, ny1, nx2, ny2)] > cnt + 1:
                        dicts[(nx1, ny1, nx2, ny2)] = cnt + 1
                        q.append([cnt + 1, nx1, ny1, nx2, ny2])
                    else:
                        continue
                else:
                    dicts[(nx1, ny1, nx2, ny2)] = cnt + 1
                    q.append([cnt + 1, nx1, ny1, nx2, ny2])

            if flag1 and not flag2:
                return cnt + 1
            if flag2 and not flag1:
                return cnt + 1

    return -1

answer = bfs(coins[0][0], coins[0][1], coins[1][0], coins[1][1])
print(answer)