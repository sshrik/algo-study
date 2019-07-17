inp = input()
h = int(inp.split(" ")[0])
m = int(inp.split(" ")[1])

if m < 45:
    h -= 1
    m += 60

if h == -1:
    h = 23

print(str(h) + " " + str(m-45))
