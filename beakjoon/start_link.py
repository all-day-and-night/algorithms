from itertools import combinations

def get_point(player, data):
    result = 0
    for i in range(len(player)-1):
        for j in range(i+1, len(player)):
            result += data[player[i]][player[j]]
            result += data[player[j]][player[i]]

    return result


N = int(input())

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

player = [i for i in range(N)]



answer = int(1e9)
for cand in combinations(player, N//2):
    start = cand
    link = [i for i in player if not i in cand]

    start_score = get_point(start, data)
    link_score = get_point(link, data)

    answer = min(answer, abs(start_score - link_score))

print(answer)