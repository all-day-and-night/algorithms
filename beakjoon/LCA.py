from collections import deque

def sol(T):
    graph_child = {}
    graph_parent = {}


    for _ in range(T-1):
        parent, child = map(int, input().split())
        graph_parent[child] = parent


    a, b = map(int, input().split())

    a_parent = deque()
    b_parent = {}

    child = a
    a_parent.append(child)
    while child in graph_parent.keys():
        parent = graph_parent[child]
        a_parent.append(parent)
        child = parent

    child = b
    b_parent[child] = 1

    while child in graph_parent.keys():
        parent = graph_parent[child]
        b_parent[parent] = 1
        child = parent

    while a_parent:
        now = a_parent.popleft()
        if now in b_parent.keys():
            return now




N = int(input())
answer = []
for _ in range(N):
    T = int(input())
    answer.append(sol(T))

for ans in answer:
    print(ans)