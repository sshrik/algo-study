def divExpression(inp):
    exLen = len(inp)
    numList = []
    operList = []
    beforeNum = ""

    for i in range(0, exLen):
        if inp[i] == '+' or inp[i] == '-':
            numList.append(int(beforeNum))
            operList.append(inp[i])
            beforeNum = ""
        else:
            beforeNum += inp[i]
            
    # Add Last number.
    numList.append(int(beforeNum))

    return numList, operList

def getAllPlus(num, oper, start):
    i = start
    res = num[i]

    while i != len(oper):
        if oper[i] == '+':
            res += num[i + 1]
            i += 1
        else:
            return res, i
    return res, i

if __name__ == "__main__":
    inp = input()
    # Init value
    num, oper = divExpression(inp)
    i = 0
    result = num[0]

    while i < len(oper):
        if oper[i] == '+':
            result += num[i + 1]
            i += 1
        else:
            p, n = getAllPlus(num, oper, i + 1)
            result -= p
            i = n

    print(result)