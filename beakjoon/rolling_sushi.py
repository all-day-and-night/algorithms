from collections import deque, defaultdict

#접시 수, 초밥의 가지 수, 연속해서 먹는 접시 수, 쿠폰번호
N, d, k, c = map(int, input().split())

q = []

for _ in range(N):
    q.append(int(input()))

temp = q[:k-1]

for t in temp:
    q.append(t)

temp = defaultdict(int)


for t in q[:k]:
    temp[t] += 1

left = 0
right = k-1
answer = 0

cnt = len(temp.keys())
if c not in temp.keys():
    cnt += 1

answer = max(answer, cnt)
for i in range(N-1):
    end = i + k
    temp[q[i]] -= 1
    temp[q[end]] += 1
    if temp[q[i]] == 0:
        del temp[q[i]]
    cnt = len(temp.keys())
    if c not in temp.keys():
        cnt += 1
    answer = max(answer, cnt)

print(answer)