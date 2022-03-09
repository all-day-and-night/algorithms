import sys
from copy import deepcopy

sys.setrecursionlimit(10**6)
N = int(input())

init = list(input())
last = list(input())

lefts = []
rights = []
# 0은 왼쪽 1은 오른쪽
# 왼쪽으로 돌릴때 아래 모든 나사 회전 +방향
dp = [[0] * 2 for _ in range(N)]
costs = [0] * N
for a, b in zip(init, last):
    #b가 크면 상관 없음
    if int(b) > int(a):
        lefts.append(int(b) - int(a))
    else:
        lefts.append(10 - (int(a) - int(b)))

    if int(a) > int(b):
        rights.append(-(int(b) - int(a)))
    else:
        rights.append(-(10 - (int(b) - int(a))))



dp[0][0] = lefts[0]
dp[0][1] = rights[0]

def leftDist(a, b):
    if int(b) > int(a):
        return int(b) - int(a)
    else:
        return 10 - (int(a) - int(b))

def rightDist(a, b):
    if int(a) > int(b):
        return int(b) - int(a)
    else:
        return -(10 - (int(b) - int(a)))

min_value = int(1e9)
answer = {}

def dfs(idx, turn, result, value):
    global min_value, answer
    if idx == N:
        if value < min_value:
            min_value = value
            answer[value] = deepcopy(result)
        return value

    #left turn
    result.append(leftDist((int(init[idx]) + turn) % 10, last[idx]))
    a = dfs(idx + 1, (turn + result[-1]) % 10, result, value + abs(result[-1]))
    result.pop()
    #right turn
    result.append(rightDist((int(init[idx]) + turn) % 10, last[idx]))
    b = dfs(idx + 1, turn % 10, result, value + abs(result[-1]))
    result.pop()

    return min(a, b)



print(dfs(0, 0, [], 0))

for i, value in enumerate(answer[min_value]):
    print(i+1, value)