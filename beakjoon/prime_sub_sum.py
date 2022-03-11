import math

def get_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    a = int(input())
    if a == 1:
        print(0)
        exit(0)
    primes = [i for i in range(2, a+1) if get_prime(i)]
    answer = 0
    left = 0
    right = 0
    end = len(primes)
    temp = primes[left]

    S = [0] * end
    S[0] = primes[0]

    for i in range(1, end):
        S[i] += S[i-1] + primes[i]

    if S[-1] < a:
        print(0)
    else:
        S = [0] + S
        end = len(S)
        left = 0
        right = 0
        while right < end and left < end:
            if S[right] - S[left] == a:
                answer += 1
                right += 1
            elif S[right] - S[left] < a:
                right += 1
            elif S[right] - S[left] > a:
                if S[right] < a:
                    right += 1
                else:
                    left += 1



    print(answer)



