graph = [[] for _ in range(300002)]

# 1이 포함 0이 불포함

isin = [0] * 300002
isnot = [0] * 300002


def dfs(sales, now):
    global graph, isin, isnot

    if len(graph[now]) == 0:
        isnot[now] = 0
        isin[now] = sales[now]
        return

    isin[now] = sales[now]

    for g in graph[now]:
        dfs(sales, g)
        isin[now] += min(isin[g], isnot[g])

    min_ = int(1e9)
    min_idx = 0
    ischeck = False
    sum_ = 0
    check = [0] * len(graph[now])
    for i, g in enumerate(graph[now]):
        for j in range(len(graph[now])):
            if i == j:
                check[j] += isin[g]
            else:
                check[j] += min(isin[g], isnot[g])

    isnot[now] = min(check)

    return


def solution(sales, links):
    global graph, isin, isnot
    answer = 0

    for a, b in links:
        graph[a - 1].append(b - 1)

    dfs(sales, 0)
    return min(isin[0], isnot[0])

