"""
dfs로 풀 수 있을 것이라 예상했지만 시간초과에 의해 비트마스킹으로 하려고 한다.

비트마스킹도 반드시 알아야 하는 알고리즘 풀이법이기 때문에

꼭 연습하는 것을 추천한다.
"""

from collections import Counter
from itertools import combinations

answer = 0


N, M = map(int, input().split())

if M < 5:
    print(0)
else:
    M -= 5
    nece_chars = {'a', 'n', 't', 'i', 'c'}
    input_chars = []
    alpha = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z')+1))) -nece_chars)
    )}
    cnt = 0
    for _ in range(N):
        tmp = 0
        for c in set(input()) - nece_chars:
            tmp |= (1 << alpha[c])
        input_chars.append(tmp)

    power_by_2 = (2**i for i in range(21))

    for comb in combinations(power_by_2, M):
        test = sum(comb)

        ct = 0
        for cb in input_chars:
            if test & cb == cb:
                ct += 1

        cnt = max(cnt, ct)
    print(cnt)



