"""
우선순위 큐로 중간값을 찾는 문제다.

배열을 2개를 두고

하나는 중간값보다 작거나 같은 것

하나는 중간값보다 큰 것을 저장해서

각각의 최대값과 최소값을 비교해서 배열의 크기를 유지한다.

중간값은 중간값보다 작거나 같은 것을 저장하는 max 힙의 최대값을 출력한다.
"""

from heapq import heappush, heappop

N = int(input())


#a는 중간값보다 작은 수
#b는 중간값보다 큰 수
a = []
b = []


answer = []
for _ in range(N):
    c = int(input())

    if len(a) == len(b):
        heappush(a, -c)
    else:
        heappush(b, c)

    if not b:
        answer.append(-a[0])
        continue

    if -a[0] > b[0]:
        n = -heappop(a)
        m = heappop(b)
        heappush(a, -m)
        heappush(b, n)
    answer.append(-a[0])

for ans in answer:
    print(ans)
