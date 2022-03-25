N = int(input())

data = list(map(int, input().split()))

M = int(input())

def sol():
    if sum(data) <= M:
        return max(data)

    start = 0
    end = M
    answer = 0
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in data:
            if i > mid:
                cnt += mid
            else:
                cnt += i

        if cnt > M:
            end = mid - 1

        else:
            answer = mid
            start = mid + 1

    return answer

print(sol())