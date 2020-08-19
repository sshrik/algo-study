NO_PRINT = 0
PRINT = 1

def setNull(pList, x, y, N):
    for i in range(x, x + N):
        for j in range(y, y + N):
            pList[i][j] = NO_PRINT

def printFunction(pList, x, y, N):
    if N == 3:
        pList[x + 1][y + 1] = NO_PRINT
    else:
        newN = int(N/3)
        for i in range(0, 3):
            for j in range(0, 3):
                if i == 1 and j == 1:
                    setNull(pList, x + newN, y + newN, newN)
                else:
                    printFunction(pList, x + newN * i, y + newN * j, newN)

def printList(pList, N):
    for i in range(0, N):
        for j in range(0, N):
            print("*", end="") if pList[i][j] == PRINT else print(" ", end="")
        print("")

if __name__ == "__main__":
    N = int(input())
    pList = []
    for _ in range(0, N):
        pList.append([])
    for i in range(0, N):
        for _ in range(0, N):
            pList[i].append(PRINT)
    printFunction(pList, 0, 0, N)
    printList(pList, N)