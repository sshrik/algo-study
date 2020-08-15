def dungCalc(w1, h1, w2, h2):
    # If 1 is bigger, return 1, 2 is bigger return -1, else return 0.
    if w1 > w2 and h1 > h2:
        return 1
    elif w1 < w2 and h1 < h2:
        return -1
    else:
        return 0

def calcLargerDung(wL, hL, ind):
    count = 1
    for ii in range(0, len(wL)):
        if ii != ind and dungCalc(wL[ii], hL[ii], wL[ind], hL[ind]) == 1:
            count += 1
    return count

pNum = int(input())
wList = []  # weight
hList = []  # height

for i in range(0, pNum):
    inp = input().split(" ")
    wList.append(int(inp[0]))
    hList.append(int(inp[1]))

for i in range(0, pNum):
    print(calcLargerDung(wList, hList, i), end = " ")
