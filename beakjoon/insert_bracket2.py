import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())

data = list(input())

nums = [int(data[i]) for i in range(N) if i % 2 == 0]
opers = [data[i] for i in range(N) if i % 2 == 1]



def calc(a, b, oper):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    else:
        return a * b

def dfs(i, value):
    if i == N//2:
        return value
    result = -int(1e9)
    result = max(result, dfs(i+1, calc(value, nums[i+1], opers[i])))

    if i+2 <= N//2:
        temp = calc(nums[i+1], nums[i+2], opers[i+1])
        result = max(result, dfs(i+2, calc(value, temp, opers[i])))

    return result

print(dfs(0, nums[0]))



