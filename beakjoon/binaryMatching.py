import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def dfs(x):
    for i in tasks[x]:
        if not check[i]:
            check[i] = True
            if visited[i] == -1 or dfs(visited[i]):
                visited[i] = x
                return True
    return False

tasks = []

for _ in range(N):
    tasks.append(list(map(int, input().split()))[1:])

result = 0
visited = [-1] * (M+1)

for i in range(N):
    check = [False] * (M+1)
    if dfs(i):
        result += 1

print(result)