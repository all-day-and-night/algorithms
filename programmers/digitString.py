def solution(s):
    answer = ""
    numbers = {'z': '0', 'o': '1', 'tw': '2', 'th': '3', 'fo': '4', 'fi': '5', 'si': '6', 'se': '7', 'e': '8', 'n': '9'}
    length = {'0': 4, '1': 3, '2': 2, '3': 4, '4': 3, '5': 3, '6': 2, '7': 4, '8': 5, '9': 4}
    temp = ""
    idx = 0
    len_ = len(s)
    while idx < len_:
        temp += s[idx]
        if temp.isdigit():
            answer += temp
            idx += 1
            temp = ""
        else:
            if temp in numbers.keys():
                answer += numbers[temp]
                idx += length[numbers[temp]]
                temp = ""
            else:
                idx += 1

    return int(answer)