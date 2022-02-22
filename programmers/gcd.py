from collections import Counter


def primes(value):
    result = []

    result.append(1)

    i = 2
    while value > 1:
        if value % i == 0:
            result.append(i)
            value /= i
        else:
            i += 1

    return Counter(result)


def solution(n, m):
    answer = [1, 1]

    primes1 = primes(n)
    primes2 = primes(m)

    for key in primes1.keys():
        if key in primes2.keys():
            answer[0] *= (key ** min(primes1[key], primes2[key]))
            answer[1] *= (key ** max(primes1[key], primes2[key]))
        else:
            answer[1] *= key ** primes1[key]

    for key in primes2.keys():
        if key not in primes1.keys():
            answer[1] *= key ** primes2[key]

    return answer