def check(beginning, target, row_bit, col_bit):
    R, C = len(beginning), len(beginning[0])

    for r in range(R):
        r_check = 1 if row_bit & (1 << r) > 0 else 0
        for c in range(C):
            c_check = 1 if col_bit & (1 << c) > 0 else 0
            status =  beginning[r][c] + r_check + c_check - target[r][c]
            if status % 2 == 1:
                return False
    return True

def count(bit):
    cnt = 0
    while bit > 0:
        if bit & 1:
            cnt += 1
        bit >>= 1
    return cnt


def solution(beginning, target):
    R, C = len(beginning), len(beginning[0])

    answer = int(1e9)
    for row_bit in range(1 << R): # or 2 ** R
        for col_bit in range(1 << C): # or 2 ** C
            # check
            status = check(beginning, target, row_bit, col_bit)
            if status:
                answer = min(answer, count(row_bit) + count(col_bit))

    return answer if answer != int(1e9) else -1