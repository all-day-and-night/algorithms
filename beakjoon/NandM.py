from itertools import permutations

N, M = map(int, input().split())

cand = [i for i in range(1, N+1)]

for ans in permutations(cand, M):
    for a in ans:
        print(a, end=' ')
    print()

