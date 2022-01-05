"""
생각해보면 간단한 문제
어떤 식으로 비교할지가 관건인데
그리디 알고리즘 처럼
각 상황에서 어떤 것을 선택할 때
정답과 가까워 지는지를 보고 선택

유효숫자를 고려하지 않는다면 쉽게 풀 수 있었을 텐데
유효숫자를 고려해야 했기 때문에 굉장히 오래걸린 문제
"""

a, b = map(int, input().split())

def check(a, b, result):
    na, nb = 0, 0
    for i, r in enumerate(result[::-1]):
        if r == '*':
            na += (2 ** (i+1))
        else:
            nb += (2 ** (i+1))

    if a * (na+nb) == na * b:
        return 1
    elif abs(a * (nb + na + 1) - (na + 1) * b) < abs(a * (na+nb+1) - na * b):
        return 2
    else:
        return 3


result = []
x, y = 0,
if a / b >= 1/2:
    result.append('*')

else:
    result.append('-')



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
