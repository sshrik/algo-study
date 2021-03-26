WHITE = 0
BLUE = 1

def divideList(inpL):
    # return divided 4 part of inpL.
    NW = []
    NE = []
    SW = []
    SE = []
    l = len(inpL)
    midL = int(l / 2)

    # Fill in each list.
    for i in range(0, midL):
        NW.append(inpL[i][0:midL])
        NE.append(inpL[i][midL:])
    for i in range(midL, l):
        SW.append(inpL[i][0:midL])
        SE.append(inpL[i][midL:])
    return NW, NE, SW, SE

def countSame(inpL):
    # Return True if all same.
    start = inpL[0][0]
    l = len(inpL)

    # If only 1 list, return True.
    if l == 1:
        return True

    # If there is not all same in list, return False.
    for i in range(0, l):
        for j in range(0, l):
            if inpL[i][j] != start:
                return False
    return True

def countNum(inpL):
    white = 0
    blue = 0
    if countSame(inpL):
        if inpL[0][0] == WHITE:
            white += 1
        else:
            blue += 1
        return white, blue
    else:
        NW, NE, SW, SE = divideList(inpL)
        nwW, nwB = countNum(NW)
        neW, neB = countNum(NE)
        swW, swB = countNum(SW)
        seW, seB = countNum(SE)
        return white + nwW + neW + swW + seW, blue + nwB + neB + swB + seB

if __name__ == "__main__":
    # If in main routine.
    length = int(input())
    inpL = []

    for i in range(0, length):
        inpS = input().split(" ")
        eList = []
        for j in range(0, length):
            eList.append(int(inpS[j]))
        inpL.append(eList)
    white, blue = countNum(inpL)
    print(white)
    print(blue)