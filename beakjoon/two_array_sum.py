from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

N = int(input())
arr1 = list(map(int, input().split()))

M = int(input())
arr2 = list(map(int, input().split()))

dictA = defaultdict(int)

for i in range(N):
    for j in range(i, N):
        dictA[sum(arr1[i:j+1])] += 1

answer = 0
for i in range(M):
    for j in range(i, M):
        answer += dictA[T - sum(arr2[i:j+1])]

print(answer)
