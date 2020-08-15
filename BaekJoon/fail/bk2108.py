def getMany(arr):

    if len(maxVal) != 1:
        min1 = 4001
        min2 = 4001
        for i in range(0, len(maxVal)):
            if resNumList[maxVal[i]] < min1:
                min2 = min1
                min1 = resNumList[maxVal[i]]
            elif resNumList[maxVal[i]] < min2:
                min2 = resNumList[maxVal[i]]
        return min2
    else:
        return resNumList[maxVal[0]]

N = int(input())

inp = []
for _ in range(0, N):
    inp.append(int(input()))

inp = sorted(inp)
inpSet = list(set(inp))
length = len(inp)

sm = 0
resNumList = []
resCntList = []
    
for i in range(0, length):
    sm += inp[i] 
    if inp[i] not in resNumList:
        resNumList.append(inp[i])
        resCntList.append(1)
    else:
        resCntList[resNumList.index(inp[i])] += 1
 
maxVal = []
maxValIndx = 0

for i in range(0, len(resNumList)):
    if resCntList[i] > resCntList[maxValIndx]:
        maxVal = [i]
        maxValIndx = i
    elif resCntList[i] == resCntList[maxValIndx]:
        maxVal.append(i)

# For real round value, change type to float.
print(round(float(sm) / len(inp)))  # Average
print(inp[int(length/2)])   # Middle

if len(maxVal) != 1:
    print(resNumList[maxVal[1]])   # Count many
else:
    print(inp[maxVal[0]])   # Count many

if length != 1:
    print(inp[-1] - inp[0]) # Length
else:
    print(0)    # Length