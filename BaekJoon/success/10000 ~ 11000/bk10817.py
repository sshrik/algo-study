inp = input()
a = int(inp.split(" ")[0])
b = int(inp.split(" ")[1])
c = int(inp.split(" ")[2])

if (a >= b and a <= c) or (a >= c and a <= b):
    print(a)
elif (b >= a and b <= c) or (b >= c and b <= a):
    print(b)
else:
    print(c)
