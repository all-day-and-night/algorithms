from itertools import combinations, permutations

def calc(start, link, data):
    # start
    start_score = 0
    for cand in permutations(start, 2):
        start_score += data[cand[0]][cand[1]]

    link_score = 0
    for cand in permutations(link, 2):
        link_score += data[cand[0]][cand[1]]

    return abs(start_score - link_score)



N = int(input())

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

idx_list = [i for i in range(N)]

min_ = int(1e9)
for start in combinations(idx_list, N // 2):
    link = [i for i in idx_list if i not in start]
    min_ = min(min_, calc(list(start), link, data))
print(min_)

