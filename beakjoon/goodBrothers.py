a, b = map(int, input().split())


def infinte(a, len_):
    return a / (1 - 2 ** (-len_))


def check(a, b, result):
    na, nb = 0, 0
    for i, r in enumerate(result[::-1]):
        if r == '*':
            na += (2 ** (i))
        else:
            nb += (2 ** (i))
    if a * (na+nb) == na * b:
        return 1
    elif abs(a * (nb + na + 1) - (na + 1) * b) < abs(a * (na+nb+1) - na * b):
        return 2
    else:
        return 3




result = []
x, y = 0, 0


now = 2 ** 63
now /= 2
if a / b >= 1/2:
    result.append('*')
    x += now
else:
    result.append('-')
    y += now


for i in range(60):
    flag = check(a, b, result)
    if flag == 1:
        break
    elif flag == 2:
        result.append('*')
    elif flag == 3:
        result.append('-')



if len(result) > 60:
    print(-1)
else:
    print(''.join(result))
