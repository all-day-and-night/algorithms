def solution(n, k):
    answer = []
    fac = [0] * (n + 1)
    fac[1] = 1
    fac[0] = 1
    for i in range(2, n + 1):
        fac[i] = fac[i - 1] * i

    list_ = [i for i in range(1, n + 1)]

    while n > 0:
        f = fac[n - 1]
        answer.append(list_.pop((k - 1) // f))
        n -= 1
        k %= f

    return answer

"""
처음에 permutations으로 문제를 해결하려 했지만 효율성 문제가 있기 때문에 다른 방법을 찾았다
factorial과 배열 사이의 수학적인 식을 도출할 수 있다면 크게 어렵지 않은 문제다 
"""