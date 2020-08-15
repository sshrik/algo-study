import copy
INIT = -1

def printTool(YAnswer, YCand, stackLevel, N, checkPan=True):
    # Debugging tool.
    print("At stack Level " + str(stackLevel))
    print("YAnswer : " + str(YAnswer))
    print("YCand : " + str(YCand))

    if checkPan:
        for i in range(0, N):
            for j in range(0, N):
                if YCand[i][YAnswer[i]] == j:
                    print("O", end=" ")
                else:
                    print("_", end=" ")
            print("")
    print("")

def getNextYLoc(YAnswer, YCand, stackLevel, N):
    # End of recursion.
    if stackLevel == N:
        # printTool(YAnswer, YCand, stackLevel, N)
        return 1
    if len(YCand[stackLevel]) == 0:
        return 0

    retVal = 0
    for i in range(0, len(YCand[stackLevel])):
        # Note that YAnswer is index of each YCand list.
        YAnswer[stackLevel] = i
        tempNextCand = copy.deepcopy(YCand[stackLevel:])
        answer = YCand[stackLevel][i]
        
        # Calc Next Candidate.
        for j in range(stackLevel + 1, N + 1):
            if answer in YCand[j]:
                del YCand[j][YCand[j].index(answer)]
            if answer + (j - stackLevel - 1) + 1 in YCand[j]:
                del YCand[j][YCand[j].index(answer + (j - stackLevel - 1) + 1)]
            if answer - (j - stackLevel - 1) - 1 in YCand[j]:
                del YCand[j][YCand[j].index(answer - (j - stackLevel - 1) - 1)]

        # Add all result of count.
        retVal += getNextYLoc(YAnswer, YCand, stackLevel + 1, N)
        
        # printTool(YAnswer, YCand, stackLevel, N, False)
        # Clear.
        YAnswer[stackLevel] = INIT
        YCand = YCand[0:stackLevel] + tempNextCand

    return retVal

if __name__ == "__main__":
    N = int(input())
    YAnswer = []
    YCand = []
    for _ in range(0, N + 1):
        YAnswer.append(INIT)
        YCand.append(list(range(0, N)))
    print(getNextYLoc(YAnswer, YCand, 0, N))
    