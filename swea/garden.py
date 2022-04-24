T = int(input())

def sol(N, D):
    step = D * 2 + 1
    if N % step == 0:
        return N // step
    else:
        return N // step + 1


answer = []
for _ in range(T):
    N, D = map(int, input().split())
    answer.append(sol(N, D))

for i, ans in enumerate(answer):
    print("#%d %d" % (i+1, ans))

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, D = map(int, input().split())

    step = D * 2 + 1
    ans = 0
    if N % D == 0:
        ans = N // step
    else:
        ans = N // step + 1
        print("#%d %d" % (test_case, ans))

