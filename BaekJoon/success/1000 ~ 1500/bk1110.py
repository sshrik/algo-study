x = input()
intX = int(x)

if x < 10:
    a = 0
    b = x
else :
    b = x % 10
    a = int( ( x - b ) / 10 )

step = 0

nextNum = -1
while nextNum != intX :
    if a + b >= 10:
        nextNum = b * 10 + (a + b) % 10
    else :
        nextNum = b * 10 + (a + b)
    if nextNum < 10:
        a = 0
        b = nextNum
    else :
        b = nextNum % 10
        a = int( ( nextNum - b ) / 10 )
    step += 1

print(step)
