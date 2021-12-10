"""
직접 풀려 했지만 테스트케이스만 통과하고 히든 케이스는 통과하지 못했다
투포인터 관한 문제를 더 풀어봐야 감을 잡을 수 있을 것 같다
"""

N, M = map(int, input().split())

data = list(map(int, input().split()))

left, right = 0, M-1
max_l = data[left]
max_r = data[right]

answer = 0
while left < right:
    max_l = max(max_l, data[left])
    max_r = max(max_r, data[right])

    if max_l > max_r:
        answer += (max_r - data[right])
        right -= 1
    else:
        answer += (max_l - data[left])
        left += 1

print(answer)

"""
7 15
0 1 0 2 3 4 0 4 0 4 1 2 3 0 1
"""