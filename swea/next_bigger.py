def solution(n):
    answer = 0
    cnt = bin(n).count("1")

    for i in range(n + 1, 1000001):
        temp = bin(i).count("1")
        if temp == cnt:
            return i

