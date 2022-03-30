"""
combination으로 해결할 수 있지만

bit mask에 익숙해져보자
"""

import sys

input = sys.stdin.readline

N, S = map(int, input().split())

data = list(map(int, input().split()))

M = N // 2
N -= M

#왼쪽 서브셋

data1 = [0] * (1 << N)

for i in range(1 << N):

    for k in range(N):
        if (i & (1 << k)) > 0:
            data1[i] += data[k]

data2 = [0] * (1 << M)

for i in range(1 << M):
    for k in range(M):
        if (i & (1 << k)) > 0:
            data2[i] += data[k+N]

data1.sort()
data2.sort(reverse=True)

N = (1 << N)
M = (1 << M)

i = 0
j = 0

ans = 0

while i < N and j < M:
    if data1[i] + data2[j] == S:
        c1 = 1
        c2 = 1
        i += 1
        j += 1
        while i < N and data1[i] == data1[i-1]:
            c1 += 1
            i += 1
        while j < M and data2[j] == data2[j-1]:
            c2 += 1
            j += 1

        ans += c1 * c2

    elif data1[i] + data2[j] < S:
        i += 1

    else:
        j += 1

if S == 0:
    ans -= 1

print(ans)