from collections import deque

N, M, K = map(int, input().split())


fireballs = deque()
board = [[[] for _ in range(N)] for _ in range(N)]


for _ in range(M):
    x, y, m, s, d = list(map(int, input().split()))
    fireballs.append([x-1, y-1, m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    #파이어볼 이동
    while fireballs:
        x, y, m, s, d = fireballs.popleft()
        nx, ny = (x + s * dx[d]) % N, (y + s * dy[d]) % N
        board[nx][ny].append([m, s, d])


    for i in range(N):
        for j in range(N):
            #2개 이상일 경우
            if len(board[i][j]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(board[i][j])

                while board[i][j]:
                    _m, _s, _d = board[i][j].pop(0)
                    sum_m += _m
                    sum_s += _s

                    if _d % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1

                    if cnt_odd == cnt or cnt_even == cnt:
                        nd = [0, 2, 4, 6]
                    else:
                        nd = [1, 3, 5, 7]

                if sum_m // 5 > 0:
                    for d in nd:
                        fireballs.append([i, j, sum_m // 5, sum_s // cnt, d])

            if len(board[i][j]) == 1:
                fireballs.append([i, j] + board[i][j].pop())

print(sum([f[2] for f in fireballs]))