import math


def timeCalc(time):
    hh, mm = time.split(':')
    return int(hh) * 60 + int(mm)


def calc(fees, time):
    if time <= fees[0]:
        return fees[1]

    return fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]


def solution(fees, records):
    answer = []
    board = {}
    temp = {}
    for record in records:
        time, ID, command = record.split()
        if command == "IN":
            if ID not in board.keys():
                board[ID] = 0

            temp[ID] = timeCalc(time)
        elif command == "OUT":
            minute = abs(temp[ID] - timeCalc(time))
            del temp[ID]

            if ID in board.keys():
                board[ID] += minute

    end = timeCalc("23:59")
    for key, value in temp.items():
        board[key] += end - value

    result = []
    for key, value in board.items():
        result.append([key, calc(fees, value)])

    result.sort(key=lambda x: x[0])
    result = [x[1] for x in result]

    return result