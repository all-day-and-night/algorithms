def getValue(x, y, base, end):
    #맨아래
    result = 0
    if x == end:
        result = base - (end - y)

    #맨 오른쪽
    elif y == -end:
        result = base - (end * 2) - (end - x)

    #맨위
    elif x == -end:
        result = base - (end * 4) - (y + end)

    #맨 왼쪽
    elif y == end:
        result = base - (end * 6) - (end + x)

    return result



r1, c1, r2, c2 = map(int, input().split())
row = r2 - r1 + 1
col = c2 - c1 + 1

bases = [(i * 2 + 1) ** 2 for i in range(5001)]


board = [[0] * col for _ in range(row)]
max_num = 0
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        end = max(abs(i), abs(j))
        base = bases[end]
        temp = getValue(i, j, base, end)
        max_num = max(max_num, temp)
        board[i - r1][j - c1] = temp

max_len = len(str(max_num))
for i in range(row):
    for j in range(col):
        print(' ' * (max_len - len(str(board[i][j]))), end='')
        print(board[i][j], end=' ')
    print()


"""
여러 블로그를 참고해서 문제를 풀음
무작정 푸는 것보다 메모리와 시간 복잡도를 고려해서 푸는 습관을 들이자

경우에 따라 수학적 식을 적는 게 자료구조를 사용하는 것보다 빠를 수 있음
규칙성을 찾아 풀어보자
"""