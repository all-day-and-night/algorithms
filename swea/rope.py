N = int(input())

ropes = sorted([int(input()) for _ in range(N)])

answer = 0

sums = sum(ropes)

for i in range(N):
    answer = max(answer, ropes[i] * (N-i))


print(answer)


