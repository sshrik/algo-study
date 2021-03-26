inp = input().split(" ")
x = int(inp[0])
y = int(inp[1])
w = int(inp[2])
h = int(inp[3])

if w - x < x:
    minWidth = w - x
else:
    minWidth = x
if h - y < y:
    minHeight = h - y
else:
    minHeight = y

if minHeight < minWidth:
    print(minHeight)
else:
    print(minWidth)
