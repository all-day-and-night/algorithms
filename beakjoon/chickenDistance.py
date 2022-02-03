from itertools import combinations

def getDistance(home, chicken, visited):
    result = 0
    for x, y in home:
        min_dist = int(1e9)

        for i in visited:
            nx, ny = chicken[i]
            min_dist = min(min_dist, abs(nx - x) + abs(ny - y))

        result += min_dist

    return result

def getDistance2(home, cand):
    result = 0
    for x, y in home:
        min_dist = int(1e9)

        for nx, ny in cand:
            min_dist = min(min_dist, abs(nx - x) + abs(ny - y))

        result += min_dist

    return result


def dfs(home, chicken, visited, M, cnt, idx):
    global ans
    if cnt == M:
        ans = min(ans, getDistance(home, chicken, visited))
        return

    for i in range(idx, len(chicken)):
        if i not in visited:
            visited.append(i)
            dfs(home, chicken, visited, M, cnt + 1, idx+1)
            visited.pop()
    return


N, M = map(int, input().split())

board = []
home = []
chicken = []
for i in range(N):
    temp = list(map(int, input().split()))

    for j, what in enumerate(temp):
        if what == 1:
            home.append([i, j])
        elif what == 2:
            chicken.append([i, j])

    board.append(temp)

ans = int(1e9)


for cand in combinations(chicken, M):
    ans = min(ans, getDistance2(home, cand))

#visited = []
#dfs(home, chicken, visited, M, 0, 0)
print(ans)
