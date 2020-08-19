inp = input()
N = int(inp.split(" ")[0])
M = int(inp.split(" ")[1])

inp = input()
numList = []

for i in range(0, N):
    numList.append(int(inp.split(" ")[i]))

res = 0
upper = -1

# Choose 3 in numList to make M ( can be same but not over )
for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            res = numList[i] + numList[j] + numList[k]
            if res <= M:
                if upper < res:
                    upper = res

print(upper)
