import sys, copy
from itertools import permutations, product

input = sys.stdin.readline

def cctvRotate(cctv, i):
    result = []
    for c in cctv:
        temp = (c + i) % 4
        result.append(temp)
    return result

def count(data, N, M):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                cnt += 1

    return cnt

def dfs(cand, cctv, cidx, data_, N, M):

    result = 65
    if len(cand) == len(cidx):

        data = copy.deepcopy(data_)
        for c, idx in zip(cand, cidx):
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            cnum, x, y = idx
            ncctv = cctvRotate(cctv[cnum], c)
            for dir_ in ncctv:
                nx, ny = x, y
                while True:
                    nx, ny = nx + dx[dir_], ny + dy[dir_]
                    #범위
                    if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                        break
                    #벽
                    if data[nx][ny] == 6:
                        break

                    if data[nx][ny] == 0:
                        data[nx][ny] = -1

        return count(data, N, M)

    else:
        for i in range(4):
            cand.append(i)
            result = min(result, dfs(cand, cctv, cidx, data_, N, M))
            cand.pop()
        return result


N, M = map(int, input().split())



cctv = [
    []
    , [0]
    , [0, 2]
    , [0, 3]
    , [0, 2, 3]
    , [0, 1, 2, 3]]

data = []
cidx = []
cnum = 0
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if not(line[j] == 0 or line[j] == 6):
            cidx.append([line[j], i, j])
            cnum += 1
    data.append(line)

rotate = [0, 1, 2, 3]
result = 65

cand = []

result = dfs(cand, cctv, cidx, data, N, M)

print(result)






