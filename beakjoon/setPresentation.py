"""
흔한 union_find 문제지만
recursion의 값을 10^5로 설정하지 않으면
오류가 생겨 시간을 할애함

"""
import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline
N, M = map(int, input().split())
parent = [i for i in range(N+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b




answer = []
for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)

    else:
        if find(a) == find(b):
            answer.append("YES")
        else:
            answer.append("NO")

for ans in answer:
    print(ans)

