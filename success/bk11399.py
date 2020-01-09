N = int(input())
inp = input().split(" ")

waitList = []
for i in range(0, N):
    waitList.append(int(inp[i]))

waitList.sort()
addUp = 0

for i in range(0, N):
    addUp += waitList[i] * (N - i)

print(addUp)