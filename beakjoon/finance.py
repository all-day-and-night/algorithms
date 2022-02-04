from collections import deque


N, M, K = map(int, input().split())

A = []
board = [[5] * N for _ in range(N)]


for _ in range(N):
    A.append(list(map(int, input().split())))

tree = [[deque() for _ in range(N)] for _ in range(N)]
dead_tree = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, input().split())
    tree[x-1][y-1].append(age)


def spring_summer(board, N, tree, dead_tree):
    for i in range(N):
        for j in range(N):
            len_ = len(tree[i][j])
            for k in range(len_):
                if board[i][j] < tree[i][j][k]:
                    for _ in range(k, len_):
                        dead_tree[i][j].append(tree[i][j].pop())
                    break

                else:
                    board[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1

    for i in range(N):
        for j in range(N):
            while dead_tree[i][j]:
                board[i][j] += dead_tree[i][j].pop() // 2


def fall_winter(A, board, N, tree):
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]

    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx, ny = i + dx[l], j + dy[l]
                        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                            continue

                        tree[nx][ny].appendleft(1)

            board[i][j] += A[i][j]

for _ in range(K):
    spring_summer(board, N, tree, dead_tree)
    fall_winter(A, board, N, tree)


result = 0


for i in range(N):
    for j in range(N):
        result += len(tree[i][j])

print(result)

