def addType(temp):
    result = []

    while temp:
        if temp[-1].isalpha():
            break
        if temp[-1] == ']':
            temp.pop()
            result.append('[')
        elif temp[-1] == '[':
            temp.pop()
            result.append(']')
        else:
            result.append(temp.pop())
    return ''.join(result) + " " + ''.join(temp)

data = input()
data = data.split()

data_list = []

common = data[0]
data = data[1:]
for d in data:
    temp = list(d)
    temp.pop()

    temp2 = common + addType(temp) + ";"
    print(temp2)
