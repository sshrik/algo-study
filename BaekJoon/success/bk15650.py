# Get M, N Number
INIT = -1

def isFull(answerStack, N):
    # If answerStack does not has INIT value, return True.
    for i in range(0, N):
        if answerStack[i] == INIT:
            return False
    return True

def printAnswer(answerStack, nextCand):
    for i in range(0, len(answerStack)):
        print(nextCand[i][answerStack[i]], end=" ")
    print("") # For enter,

def nextMNCandidate(N, answerStack, nextCand, stackLevel):
    for i in range(0, len(nextCand[stackLevel])):
        answerStack[stackLevel] = i
        if stackLevel > 0:
            if nextCand[stackLevel - 1][answerStack[stackLevel - 1]] > nextCand[stackLevel][answerStack[stackLevel]]:
                answerStack[stackLevel] = INIT
                continue
        if isFull(answerStack, N):
            printAnswer(answerStack, nextCand)
        else:
            nextCand[stackLevel + 1 ] = nextCand[stackLevel][0:i] + nextCand[stackLevel][i+1:]
            nextMNCandidate(N, answerStack, nextCand, stackLevel + 1)
            nextCand[stackLevel + 1] = []
        answerStack[stackLevel] = INIT

if __name__ == "__main__":
    inp = input().split(" ")
    M = int(inp[0])
    N = int(inp[1])
    answerStack = []
    nextCand = [list(range(1, M + 1))]
    for _ in range(0, N):
        answerStack.append(INIT)
    for _ in range(1, N):
        nextCand.append([])
    nextMNCandidate(N, answerStack, nextCand, 0)
