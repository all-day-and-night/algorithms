from collections import deque
N, L, R = map(int, input().split())

def bfs(data, N, L, R):
    mig_cnt = 0
    check = [[0] * N for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(N):
        for j in range(N):
            if check[i][j] != 0:
                continue
            q = deque()
            temp = []
            q.append([i, j])
            temp.append([i, j, data[i][j]])
            check[i][j] = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                        continue
                    if check[nx][ny] != 0:
                        continue
                    if L <= abs(data[x][y] - data[nx][ny]) <= R:
                        q.append([nx, ny])
                        check[nx][ny] = 1
                        temp.append([nx, ny, data[nx][ny]])
            if len(temp) > 1:
                mig_cnt+=1
                cnt = 0
                for k in range(len(temp)):
                    x, y, num = temp[k]
                    cnt += num
                mig = cnt // len(temp)

                for k in range(len(temp)):
                    x, y, num = temp[k]
                    data[x][y] = mig
    return mig_cnt





data = []
for _ in range(N):
    data.append(list(map(int, input().split())))


cnt = 0
while 1:
    if bfs(data, N, L, R) != 0:
        cnt += 1
    else:
        break
print(cnt)