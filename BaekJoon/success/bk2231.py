def makeNext(num):
    sNum = str(num)
    res = num

    for i in range(0, len(sNum)):
        res += int(sNum[i])
    
    return res

def makeBefore(num):
    l = len(str(num))
    maxIndx = l * 9
    res = []
    smallRes = num

    for i in range(1, maxIndx + 1):
        if num - i < 1:
            break
        elif makeNext(num - i) == num:
            res.append(num - i)
            if smallRes > num - i:
                smallRes = num - i

    return res, smallRes

inp = int(input())
for inp in range(1, 100000):
    beforeStack = []
    res, smallRes = makeBefore(inp)
    if len(res) == 0:
        print(0) 
    else:
        print(smallRes)

#beforeStack += res
#
#if len(res) == 0:
#    print("0")
#else:
#    while len(beforeStack) != 0:
#        nowNum = beforeStack[0]
#        del beforeStack[0]
#        addStack, snum = makeBefore(nowNum)
#        beforeStack += addStack
#        if smallRes > snum:
#            smallRes = snum

#
#maxNum = 1000000
#NMade = []
#
#for i in range(0, maxNum + 1):
#    NMade.append(0)
#
#for i in range(1, maxNum + 1):
#    if NMade[i] != 0:
#        continue
#    nowNum = i
#    nextNum = makeNext(nowNum)
#    while nextNum <= maxNum:
#        #print(str(nowNum) + " to " + str(nextNum))
#        NMade[nextNum] = nowNum
#        nowNum = nextNum
#        nextNum = makeNext(nowNum)
