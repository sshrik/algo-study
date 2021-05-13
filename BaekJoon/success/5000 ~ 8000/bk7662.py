# https://www.acmicpc.net/problem/7662
import sys
import heapq
fastio = sys.stdin.readline

def insert(minTree, maxTree, validDict, value):
    if value in validDict:
        validDict[value] += 1
    else:
        validDict[value] = 1
    heapq.heappush(minTree, value)
    heapq.heappush(maxTree, value * -1)

def popMin(minTree, validDict):
    minValue = None
    while len(minTree) != 0:
        minValue = heapq.heappop(minTree)
        if validDict[minValue] > 0:
            validDict[minValue] -= 1
            break
        minValue = None
    return minValue
    
def popMax(maxTree, validDict):
    maxValue = None
    while len(maxTree) != 0:
        maxValue = heapq.heappop(maxTree)
        if validDict[-1 * maxValue] > 0:
            validDict[-1 * maxValue] -= 1
            break
        maxValue = None
    return maxValue

if __name__ == "__main__":
    T = int(fastio().rstrip())
    for t in range(T):
        minTree = []
        maxTree = []
        validDict = {}
        K = int(fastio().rstrip())
        for k in range(K):
            inp = fastio().rstrip().split(" ")
            if inp[0] == "I":
                insert(minTree, maxTree, validDict, int(inp[1]))
            else:
                if int(inp[1]) == -1:
                    popMin(minTree, validDict)
                else:
                    popMax(maxTree, validDict)
        if len(minTree) == 0 or len(maxTree) == 0:
            print("EMPTY")
        else:
            minValue = popMin(minTree, validDict)
            if minValue == None:
                print("EMPTY")
            else:
                insert(minTree, maxTree, validDict, minValue)
                maxValue = popMax(maxTree, validDict)
                if maxValue == None:
                    print("EMPTY")
                else:
                    print(-1 * maxValue, minValue)
