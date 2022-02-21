"""
분할정복

경우에 따라서 연산방법이나 조건을 다르게 해서 풀면 ㅇㅋ

항상 N이 많을 경우 logN으로 바꾸는 법을 고려하자
"""

def power(a, b, c):
    if b == 1:
        return a % c
    else:
        temp = power(a, b//2, c)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c



a, b, c = map(int, input().split())

answer = power(a, b, c)

print(answer)

