N, M = map(int, input().split())

non_seen = set([input() for _ in range(N)])
non_heard = set([input() for _ in range(M)])


answer = []

for a in non_seen:
    if a in non_heard:
        answer.append(a)

answer.sort()

print(len(answer))
for ans in answer:
    print(ans)
