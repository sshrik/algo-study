def calcNextDp(dpList, ind, wL, vL):
    max = -1

    return max

inp = input().split(" ")
N = int(inp[0])
K = int(inp[1])

vList = []
wList = []

for n in range(0, N):
    inp = input().split(" ")
    wList.append(int(inp[0]))
    vList.append(int(inp[1]))

# dp[w] == w weight`s largest value.
dp = [0 for _ in range(0, K + 1)]

for i in range(0, K):
    calcNextDp(dp, i, wList, vList)

print(dp[-1])


'''
vAdd = [0]
wAdd = [0]

max = -1

for n in range(0, N):
    inp = input().split(" ")
    W = int(inp[0])
    V = int(inp[1])
    newVAdd = []
    newWAdd = []

    for i in range(0, len(vAdd)):
        if wAdd[i] + W <= K:
            newVAdd.append(vAdd[i] + V)
            newWAdd.append(wAdd[i] + W)
            if vAdd[i] + V > max:
                max = vAdd[i] + V
    
    vAdd += newVAdd
    wAdd += newWAdd
    print(vAdd)
    print(wAdd)
    
print(max)
'''