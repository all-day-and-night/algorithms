def divide(sx, sy, ex, ey, x, y, value):

    if sx == ex and sy == ey:
        return value

    mx, my = (sx + ex) / 2, (sy + ey) / 2

    result = 0
    half = 0
    if ex - sx == 1:
        half = 1
    else:
        half = (ex - sx + 1) // 2
    plus = half ** 2
    #1
    if x < mx and y < my:
        result = divide(sx, sy, ex - half, ey - half, x, y, value)
    elif x < mx and y > my:
        result = divide(sx, sy + half, ex - half, ey, x, y, value + plus)
    elif x > mx and y < my:
        result = divide(sx + half, sy, ex, ey - half, x, y, value + plus * 2)
    elif x > mx and y > my:
        result = divide(sx + half, sy + half, ex, ey, x, y, value + plus * 3)

    return result

N, r, c = map(int, input().split())

max_ = (2 ** N) - 1
sx, sy = 0, 0
ex, ey = max_, max_

print(divide(sx, sy, ex, ey, r, c, 0))