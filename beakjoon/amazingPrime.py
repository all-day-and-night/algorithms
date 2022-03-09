import math

def get_prime(v):
    for i in range(2, int(math.sqrt(v)) + 1):
        if v % i == 0:
            return False
    return True


N = int(input())

primes = [[] for _ in range(N+1)]

for i in range(2, 10):
    if get_prime(i):
        primes[0].append(i)

adds = [1, 3, 7, 9]
for i in range(1, N):
    for p in primes[i-1]:
        temp = p * 10
        for a in adds:
            value = temp + a
            if get_prime(value):
                primes[i].append(value)

for prime in primes[N-1]:
    print(prime)

