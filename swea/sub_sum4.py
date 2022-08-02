import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = list(map(int, input().split()))

for i in range(1, N):
    data[i] += data[i-1]

data = [0] + data

for _ in range(M):
    a, b = map(int, input().split())
    print(data[b] - data[a-1])

