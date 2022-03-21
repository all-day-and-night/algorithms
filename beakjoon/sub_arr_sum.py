import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N, S = map(int, input().split())

data = list(map(int, input().split()))
check = [0] * N

def dfs(value, depth, cnt):
    global N, S
    if depth == N:
        if value == S and cnt > 0:
            return 1
        else:
            return 0

    result = 0
    result += dfs(value + data[depth], depth + 1, cnt + 1)
    result += dfs(value, depth + 1, cnt)

    return result



answer = dfs(0, 0, 0)
print(answer)