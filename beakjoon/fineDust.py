#pypy로 채점
N, M, T = map(int, input().split())

def circulate(data, fresh, N, M):
    result = 0
    fx1, fy1 = fresh[0]
    fx2, fy2 = fresh[1]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir1 = 0
    #위에 것
    x = fx1
    y = fy1 + 1
    prev = data[x][y]
    data[x][y] = 0
    while 1:
        #종료
        nx, ny = x + dx[dir1], y + dy[dir1]
        if nx == fx1 and ny == fy1:
            result += prev
            break
        if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
            dir1 = (dir1-1) % 4
            continue
        temp = data[nx][ny]
        data[nx][ny] = prev
        prev = temp
        x, y = nx, ny
    #아래 것
    dir2 = 0
    x, y = fx2, fy2 + 1
    prev = data[x][y]
    data[x][y] = 0
    while 1:
        # 종료
        nx, ny = x + dx[dir2], y + dy[dir2]
        if nx == fx2 and ny == fy2:
            result += prev
            break
        if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
            dir2 = (dir2 + 1) % 4
            continue
        temp = data[nx][ny]
        data[nx][ny] = prev
        prev = temp
        x, y = nx, ny
    return result

def diffuse(data, N, M):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    check = [[0] * M for _ in range(N)]
    diff = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if data[i][j] > 4:
                move = []
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                        continue
                    if data[nx][ny] == -1:
                        continue
                    move.append([nx, ny])

                #move
                cnt = len(move)
                dif = data[i][j] // 5
                for x, y in move:
                    diff[x][y] += dif
                data[i][j] -= (dif * cnt)

    for i in range(N):
        for j in range(M):
            data[i][j] += diff[i][j]





data = []
fresh = []
result = 0
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == -1:
            fresh.append([i, j])
        if temp[j] > 0:
            result += temp[j]
    data.append(temp)

for i in range(T):
    diffuse(data, N, M)
    result -= circulate(data, fresh, N, M)

print(result)