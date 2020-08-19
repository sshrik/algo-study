while True:
    try:
        inp = input()
        a = int(inp.split(" ")[0])
        b = int(inp.split(" ")[1])
        if a == 0 and b == 0:
            break
        else:
            print(a+b)
    except:
        break
