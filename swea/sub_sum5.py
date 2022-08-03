import sys

input = sys.stdin.readline

N, M = map(int, input().split())

data = [[0] * (N+1)]
for _ in range(N):
    temp = list(map(int, input().split()))
    data.append([0] + temp)



for i in range(1, N+1):
    for j in range(1, N+1):
        data[i][j] += data[i-1][j] + data[i][j-1] - data[i-1][j-1]

def solution(x, y, nx, ny):
    return data[nx][ny] - data[nx][y-1] - data[x-1][ny] + data[x-1][y-1]
    

for _ in range(M):
    x, y, nx, ny = map(int, input().split())
    print(solution(x, y, nx, ny))


