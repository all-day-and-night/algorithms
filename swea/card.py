from collections import Counter
N = int(input())

cards = [int(input()) for _ in range(N)]

cnts = Counter(cards)
keys = sorted(list(cnts.keys()))

max_ = max(cnts.values())

for key in keys:
    if cnts[key] == max_:
        print(key)
        break

