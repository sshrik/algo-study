
f = open("objects.json", "r")
ll = f.readlines()
f.close()

for l in ll:
    obj = l.split(", ")
    for o in obj:    
        print(o)
        input()

