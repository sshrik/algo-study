def countMin(view, startX, startY):
    wStartCount = 0
    bStartCount = 0

    wStartCheck = 'W'

    for k in range(startX, startX + 8):
        for l in range(startY, startY + 8):
            if view[k][l] == wStartCheck:
                bStartCount += 1
            else:
                wStartCount += 1
            # Toggle W / B check.
            if l != startY + 7:
                wStartCheck = 'B' if wStartCheck == 'W' else 'W'
    return bStartCount if wStartCount > bStartCount else wStartCount

inp = input().split(" ")
x = int(inp[0])
y = int(inp[1])

space = []
for i in range(0, x):
    space.append(input())

minRes = x * y

for i in range(0, x - 7):
    for j in range(0, y - 7):
        res = countMin(space, i, j)
        minRes = res if res < minRes else minRes

print(minRes)