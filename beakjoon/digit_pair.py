N = int(input())

minus = []
plus = []
answer = 0
for _ in range(N):
    temp = int(input())
    if temp <= 0:
        minus.append(temp)
    else:
        if temp == 1:
            answer += 1
        else:
            plus.append(temp)


minus.sort()
plus.sort(reverse=True)

m = 0
temp = 0
for i in range(len(minus)):
    if i % 2 == 0:
        temp += minus[i]
    else:
        temp *= minus[i]
        m += temp
        temp = 0

m += temp

n = 0
temp = 0

for i in range(len(plus)):
    if i % 2 == 0:
        temp += plus[i]
    else:
        temp *= plus[i]
        n += temp
        temp = 0

n += temp

answer += n + m
print(answer)




