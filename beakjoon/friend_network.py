from collections import defaultdict

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent, cnt):
    a = find(a, parent)
    b = find(b, parent)

    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]

N = int(input())

for _ in range(N):
    M = int(input())

    parent = {}
    cnt = {}
    for _ in range(M):
        a, b = input().split()

        if a not in parent.keys():
            parent[a] = a
            cnt[a] = 1

        if b not in parent.keys():
            parent[b] = b
            cnt[b] = 1

        union(a, b, parent, cnt)
        print(cnt[parent[a]])

