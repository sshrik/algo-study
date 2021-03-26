# Calc least number to make K won.
inp = input().split(" ")
N = int(inp[0])
K = int(inp[1])
wonList = []

# modList mean less number of wonList.
for _ in range(0, N):
    inp = int(input())
    wonList.append(inp)

answer = 0

# Make K with add up of modList.
for i in range(N - 1, -1, -1):
    if K >= wonList[i]:
        # print("Use " + str(wonList[i]) + " won : " + str(int(K/wonList[i])))
        answer += int(K/wonList[i])
        K = K % wonList[i]
    if K == 0:
        break

print(answer)