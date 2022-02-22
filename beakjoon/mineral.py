"""
빡 구현 문제

테케를 직접 생각해서 푸는 습관을 들이자
"""

from collections import deque

N, M = map(int, input().split())

board = []

for i in range(N):
    temp = list(input())
    board.append(temp)

T = int(input())
heights = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def getCluster(x, y, board, check):

    q = deque()
    cluster = set()
    q.append([x, y])
    bottom = 0
    check[x][y] = 1
    while q:
        x, y = q.popleft()
        bottom = max(bottom, x)

        cluster.add((x, y))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue

            if board[nx][ny] == 'x' and check[nx][ny] == 0:
                q.append([nx, ny])
                check[nx][ny] = 1

    return cluster, bottom


def throws(height, board, dir):
    if dir % 2 == 0:
        for i in range(M):
            if board[height][i] == 'x':
                board[height][i] = '.'
                return True

    else:
        for i in range(M-1, -1, -1):
            if board[height][i] == 'x':
                board[height][i] = '.'
                return True

    return False

def getHeight(board, cluster):
    h = 1

    bottoms = [-1] * M

    for x, y in cluster:
        bottoms[y] = max(bottoms[y], x)

    bottom = []
    for y, x in enumerate(bottoms):
        if x == -1:
            continue
        bottom.append([x, y])

    while True:
        for x, y in bottom:
            nx, ny = x + h, y

            if board[nx][ny] == 'x':
                return h-1

            if nx == N-1:
                return h

            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue



        h += 1

def getDown(board, h, cluster):
    for x, y in cluster:
        board[x+h][y] = 'x'

for dir, h in enumerate(heights):
    if throws(N - h, board, dir):
        check = [[0] * M for _ in range(N)]
        isend = False
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'x' and check[i][j] == 0:
                    cluster, bottom = getCluster(i, j, board, check)
                    if bottom != N-1:
                        for x, y in cluster:
                            board[x][y] = '.'

                        h = getHeight(board, cluster)
                        getDown(board, h, cluster)
                        isend = True
                        break
            if isend:
                break

for b in board:
    for a in b:
        print(a, end='')
    print()



"""
8 8
........
........
...x.xx.
...xxx..
..xxx...
..x.xxx.
..x...x.
.xxxxxx.
5
6 6 4 3 1
"""



