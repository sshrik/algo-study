inp = input()
a = int(inp.split(" ")[0])
b = int(inp.split(" ")[1])

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")
