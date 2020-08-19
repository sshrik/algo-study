def checkIncrease(inp):
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    if a > b:
        return a-b == b-c
    else:
        return b-a == c-b

inp = input()
ans = 0

if int(inp) < 100:
    print(inp)
else:
    ans = 99
    for i in range(100, int(inp) + 1):
        if checkIncrease(str(i)):
            ans += 1
    print(ans)

