"""
문제가 정확히 이해가 가지 않아서 고생을 많이 함
다른 사람들의 풀이를 보니 굉장히 간단하게 구현 가능하지만
이해하지 못해서 어려움을 겪음

접근 방법:
1. 처음과 끝의 값은 끝까지 남길 수 있음
2. 가운데 값은 minFront = 첫번째 값, minRear = 마지막 값에서 출발하여 자기보다 작은 수를 남길 수 있다.
->한쪽에서 자신이 가장 작은 값이면 1번은 자기보다 큰 것을 터뜨릴 수 있기 때문에 가능하다.
"""

def solution(a):
    result = [0 for _ in a]
    minFront, minRear = int(1e9), int(1e9)

    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = 1
        if a[-1 - i] < minRear:
            minRear = a[-1 - i]
            result[-1 - i] = 1

    return sum(result)