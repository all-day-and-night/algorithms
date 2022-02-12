
def getIdx(value):
    x = value // 3
    y = value % 3
    return x, y

def getDistance(now, next_):
    x, y = now
    nx, ny = next_

    return abs( x -nx) + abs(y - ny)

def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    buttons = {1 :'L', 4 :'L', 7 :'L', 3 :'R', 6 :'R', 9 :'R', 2 :'M', 5 :'M', 8 :'M', 0 :'M'}

    for num in numbers:
        next_ = buttons[num]
        print(num, left, right)
        if next_ == 'L':
            answer += 'L'
            left = num
        elif next_ == 'R':
            answer += 'R'
            right = num
        else:
            if num == 0:
                num = 11
            left_idx = getIdx(lef t -1)
            right_idx = getIdx(righ t -1)
            now_idx = getIdx(nu m -1)

            left_dist = getDistance(now_idx, left_idx)
            right_dist = getDistance(now_idx, right_idx)

            if left_dist > right_dist:
                answer += 'R'
                right = num
            elif left_dist < right_dist:
                answer += 'L'
                left = num
            else:
                if hand == "right":
                    answer += 'R'
                    right = num
                else:
                    answer += "L"
                    left = num
    return answer