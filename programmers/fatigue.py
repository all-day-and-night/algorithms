#간단한 DFS문제였음

def dfs(remain, dungeons, check, cnt):
    if len([w for w, _ in dungeons if w <= remain]) == 0 or len([w for w in check if w == 0]) == 0:
        return cnt

    result = 0
    for i in range(len(dungeons)):
        if remain >= dungeons[i][0] and check[i] == 0:
            check[i] = 1
            result = max(result, dfs(remain - dungeons[i][1], dungeons, check, cnt + 1))
            check[i] = 0
    return result


def solution(k, dungeons):
    # 방문, 남은 피로도
    check = [0] * len(dungeons)

    result = dfs(k, dungeons, check, 0)

    return result