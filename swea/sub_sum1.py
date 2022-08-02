import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M, K = map(int, input().split())

data = []
tree = [0] * (3000000)

def init(node, start, end):
    #리프 노드인 경우
    if start == end:
        tree[node] = data[start]
        return tree[node]

    mid = (start + end) // 2

    tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]


"""
구간 합 구하기
node의 구간 start, end
배열에서 합을 구해야 하는 구간 left, right
"""
def sub_sum(node, start, end, left, right):
    #구간이 겹치지 않기 때문에 return 0
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return sub_sum(node * 2, start, (start + end) // 2, left, right) + sub_sum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff

    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)



for _ in range(N):
    data.append(int(input()))

init(1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        b = b-1
        diff = c - data[b]
        data[b] = c
        update(1, 0, N-1, b, diff)
    else:
        print(sub_sum(1, 0, N-1, b-1, c-1))






