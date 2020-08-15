inp = input().split(" ")

A = int(inp[0])
B = int(inp[1])
C = int(inp[2])

if C > B:
    print(int(A/(C-B)) + 1)
else:
    print(-1)