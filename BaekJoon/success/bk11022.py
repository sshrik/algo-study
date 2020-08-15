T = int(input())

for t in range(0, T): 
    inp = input()
    a = int(inp.split(" ")[0])
    b = int(inp.split(" ")[1])

    print("Case #" + str(t + 1) + ": " + str(a) + " + " + str(b) + " = "  + str(a + b))
