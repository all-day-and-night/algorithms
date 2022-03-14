N = int(input())

edges = list(map(int, input().split()))

costs = list(map(int, input().split()))

left = 0
right = 1

now = costs[left]

answer = 0
len_ = 0
for i in range(1, len(costs)):
    len_ += edges[i - 1]

    if now > costs[i]:
        answer += len_ * now
        now = costs[i]
        len_ = 0

if len_ != 0:
    answer += now * len_

print(answer)



