"""
... 아니 순서 때문에 틀리다니......

가장 기본적인 재귀함수를 사용한 dfs니까 항상 생각하자
"""

N = int(input())

nums = list(map(int, input().split()))

opers = list(map(int, input().split()))

max_, min_ = -int(1e12), int(1e12)

def dfs(depth, total, plus, minus, multiply, divide):
    global max_, min_

    if depth == N:
        max_ = max(total, max_)
        min_ = min(total, min_)

    if plus:
        dfs(depth + 1, total + nums[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide-1)

dfs(1, nums[0], opers[0], opers[1], opers[2], opers[3])


print(max_)
print(min_)