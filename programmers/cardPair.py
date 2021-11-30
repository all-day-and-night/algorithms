import copy

from itertools import permutations
from collections import deque


def ctrl_move(board, fx, fy, dx, dy):
    x, y = fx, fy
    while True:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx > 3 or ny > 3:
            return x, y
        else:
            if board[nx][ny] != 0:
                return nx, ny
            x, y = nx, ny


def bfs(board, fx, fy, tx, ty):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 처음에 시작할때 주의 이거 때문에 시간 엄청 소모함
    if fx == tx and fy == ty:
        board[fx][fy] = 0
        return 1

    INF = int(1e9)
    distance = [[INF] * 4 for _ in range(4)]
    visited = [[0] * 4 for _ in range(4)]

    q = deque()
    x, y = fx, fy
    q.append([x, y])
    distance[x][y] = 0
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny] == 0:

                if distance[nx][ny] > distance[x][y] + 1:
                    distance[nx][ny] = distance[x][y] + 1
                    if nx == tx and ny == ty:
                        board[nx][ny] = 0
                        return distance[nx][ny] + 1  # press enter
                    q.append([nx, ny])

            nx, ny = ctrl_move(board, x, y, dx[i], dy[i])
            if distance[nx][ny] > distance[x][y] + 1:
                distance[nx][ny] = distance[x][y] + 1
                if nx == tx and ny == ty:
                    board[nx][ny] = 0
                    return distance[nx][ny] + 1  # press enter
                q.append([nx, ny])


def sol(board, r, c, order, cards, dist):
    global answer
    if len(order) == 0:
        answer = min(answer, dist)
        return

    now = order[-1]

    left, right = cards[now]

    d1 = bfs(board, r, c, left[0], left[1])
    d2 = bfs(board, left[0], left[1], right[0], right[1])
    order.pop()
    del cards[now]

    sol(board, right[0], right[1], order, cards, dist + d1 + d2)
    # 이전상태로 초기화
    board[left[0]][left[1]] = now
    board[right[0]][right[1]] = now
    order.append(now)
    cards[now] = [left, right]

    d1 = bfs(board, r, c, right[0], right[1])
    d2 = bfs(board, right[0], right[1], left[0], left[1])

    order.pop()
    del cards[now]
    sol(board, left[0], left[1], order, cards, dist + d1 + d2)
    # 이전 상태로 초기화
    board[left[0]][left[1]] = now
    board[right[0]][right[1]] = now
    order.append(now)
    cards[now] = [left, right]


def solution(board, r, c):
    global answer
    N = 4
    answer = int(1e9)
    cards = {}
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                if board[i][j] in cards.keys():
                    cards[board[i][j]].append([i, j])
                else:
                    cards[board[i][j]] = [[i, j]]
    orders = [k for k, v in cards.items()]
    trace = []
    for order in list(permutations(orders)):
        # board, 현재위치 ,순서, card 위치
        sol(board, r, c, list(order), cards, 0)

    return answer