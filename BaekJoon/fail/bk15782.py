N, M = input().split(" ")
N = int(N)  # Node number.
M = int(M)  # Calc number.

nodeValue = []
childInfo = []

for _ in range(0, N - 1):
    paren, child = input().split(" ")
    paren = int(paren)
    child = int(child)
    
    while len(childInfo) < paren:
        childInfo.append([])
    childInfo[paren - 1].append([child])

while len(childInfo) < N:
    childInfo.append([])

# Reverse of index order,
for i in range(N - 1, -1, -1):
    if len(childInfo[i]) != 0:
        # If linkable child node exist,
        idx = 0
        
        # After init index value, for all childInfo[i], add direct link node`s child.
        for cc in childInfo[i] :
            # cc mean lined child node`s link information.
            # cc[0] - 1 is direct child`s index.
            if len(childInfo[cc[0] - 1]) != 0 :
                for addChild in childInfo[cc[0] - 1]:
                    # addChild is direct child`s child.
                    childInfo[i][idx] += addChild
            idx += 1

x = input().split(" ")

for i in range(0, N):
    nodeValue.append(int(x[i]))

#print(childInfo)
#print(nodeValue)

for _ in range(0, M):
    x = input().split(" ")
    if len(x) == 3:
        # Calc Operation code 2.
        calcOp = int(x[0])
        calcNum = int(x[1])
        calcNumY = int(x[2])

        nodeValue[calcNum - 1] ^= calcNumY

        for childNum in childInfo[calcNum - 1]:
            for cc in childNum:
                nodeValue[cc - 1] ^= calcNumY

    elif len(x) == 2:
        # Calc Operation code 1.
        calcOp = int(x[0])
        calcNum = int(x[1])
        res = nodeValue[calcNum - 1]
        
        for child in childInfo[calcNum - 1]:
            for cc in child:
                res ^= nodeValue[cc - 1]
        print(res)

    #print("CHILD :  " + str(childInfo))
    #print("NODE :   " + str(nodeValue))


