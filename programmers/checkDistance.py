from itertools import combinations

def getDist(x, y, nx, ny, place):
    dist = abs(x - nx) + abs(y - ny)
    if dist == 1:
        return False

    if dist == 2:
        if x == nx:
            if place[x][(y + ny) // 2] != 'X':
                return False
        if y == ny:
            if place[(x + nx) // 2][y] != 'X':
                return False
        if x != nx and y != ny:
            if place[x][ny] != 'X' or place[nx][y] != 'X':
                return False

    return True

def solution(places):

    answer = []

    for place in places:
        cands = []
        for i, place_ in enumerate(place):
            for j, p in enumerate(place_):
                if p == "P":
                    cands.append([i, j])
        isTrue = True
        for cand in combinations(cands, 2):
            left, right = cand
            x, y = left
            nx, ny = right
            if not getDist(x, y, nx, ny, place):
                isTrue = False
                break

        if isTrue:
            answer.append(1)
        else:
            answer.append(0)


    return answer







places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))