"""from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0,-1, 0]

def bfs(plates, idxs, i, j, N, M):
    check = False

    q = deque()
    q.append([i, j])
    nx, ny = 0, 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            #위 아래

            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx > N-1:
                continue

            if plates[nx][(idxs[nx] + ny) % M] != 0 and plates[nx][(idxs[nx] + ny) % M] == plates[x][(idxs[x] + y) % M]:
                q.append([nx, ny % M])
                plates[nx][(idxs[nx] + ny) % M] = 0
                check = True

    if check:
        plates[i][(idxs[i] + j) % M] = 0
        return True

    else:
        return False








N, M, T = map(int, input().split())

plates = []
idxs = [0] * N
for _ in range(N):
    plates.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        print(plates[i][(idxs[i] + j) % M], end=' ')
    print()

for _ in range(T):
    x, d, k = map(int, input().split())

    dir_ = 0
    if d == 0:
        dir_ = -1
    else:
        dir_ = 1

    for i in range(N):
        if (i + 1) % x == 0:
            idxs[i] = (dir_ * k + idxs[i]) % M

    print("before")
    for i in range(N):
        for j in range(M):
            print(plates[i][(idxs[i] + j) % M], end=' ')
        print()

    check = False
    for i in range(N):
        for j in range(M):
            if plates[i][(j + idxs[i]) % M] != 0:
                if bfs(plates, idxs, i, j, N, M):
                    check = True

    if not check:
        sum_ = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if plates[i][j] != 0:
                    cnt += 1
                    sum_ += plates[i][j]

        average = sum_ / cnt
        print("average", average)
        for i in range(N):
            for j in range(M):
                if plates[i][j] != 0:
                    if plates[i][j] > average:
                        plates[i][j] -= 1
                    elif plates[i][j] < average:
                        plates[i][j] += 1

    print("after")
    for i in range(N):
        for j in range(M):
            print(plates[i][(idxs[i] + j) % M], end=' ')
        print()

    print()

result = 0
for p in plates:
    result += sum(p)

print(result)


"""

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(plates, i, j, N, M):
    check = False
    value = plates[i][j]
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        plates[x][y] = 0
        for k in range(4):
            #위 아래
            
            nx, ny = x + dx[k], (y + dy[k] + M) % M

            if nx < 0 or nx > N-1:
                continue

            if plates[nx][ny] != 0 and plates[nx][ny] == value:
                q.append([nx, ny])

                check = True

    if check:
        #plates[i][j] = 0
        return True

    else:
        plates[i][j] = value
        return False





N, M, T = map(int, input().split())

plates = []
for _ in range(N):
    plates.append(deque(list(map(int, input().split()))))



for _ in range(T):
    x, d, k = map(int, input().split())

    dir_ = 0
    if d == 0:
        dir_ = 1
    else:
        dir_ = -1

    for i in range(N):
        if (i + 1) % x == 0:
            plates[i].rotate(k * dir_)


    check = False
    for i in range(N):
        for j in range(M):
            if plates[i][j] != 0:
                if bfs(plates, i, j, N, M):
                    check = True

    if not check:
        sum_ = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if plates[i][j] != 0:
                    cnt += 1
                    sum_ += plates[i][j]

        average = sum_ / cnt
        for i in range(N):
            for j in range(M):
                if plates[i][j] != 0:
                    if plates[i][j] > average:
                        plates[i][j] -= 1
                    elif plates[i][j] < average:
                        plates[i][j] += 1


result = 0
for p in plates:
    result += sum(p)

print(result)


