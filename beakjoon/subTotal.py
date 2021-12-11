N, S = map(int, input().split())

data = list(map(int, input().split()))

start = 0
end = 0

sum_ = 0
min_len = int(1e9)

while start < N:
    if sum_ >= S:
        min_len = min(min_len, end - start)
        sum_ -= data[start]
        start += 1

    else:
        if end > N-1:
            break
        else:
            sum_ += data[end]
            end += 1
if min_len == int(1e9):
    print(0)
else:
    print(min_len)

