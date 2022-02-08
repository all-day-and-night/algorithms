from collections import deque


def check(table, q):
    temp = list(q)

    for t in temp:
        if t > table:
            return t

    return None

N = int(input())

cards = [i for i in range(1, 2*N+1)]

S = []

for _ in range(N):
    S.append(int(input()))

G = [i for i in cards if i not in S]

S.sort()

S = deque(S)
G = deque(G)

score_s = 0
score_g = 0

turn = 0
table = 0
while S and G:
    #상근이 턴
    if turn % 2 == 0:
        if table == 0:
            table = S.popleft()
        else:
            temp = check(table, S)
            if temp == None:
                table = 0
            else:
                table = temp
                S.remove(temp)
    #근상이 턴
    else:
        if table == 0:
            table = G.popleft()
        else:
            temp = check(table, G)
            if temp == None:
                table = 0
            else:
                table = temp
                G.remove(temp)

    turn += 1


print(len(G))
print(len(S))

