x = []
y = []

for i in range(0, 3):
    inp = input().split(" ")
    x.append(int(inp[0]))
    y.append(int(inp[1]))

resX = 0
resY = 0

print(x)
print(y)

if x[0] == x[1]:
    resX = x[2]
elif x[0] == x[2]:
    resX = x[1]
else:
    resX = x[0]
    
if y[0] == y[1]:
    resY = y[2]
elif y[0] == y[2]:
    resY = y[1]
else:
    resY = y[0]

print(str(resX) + " " + str(resY))