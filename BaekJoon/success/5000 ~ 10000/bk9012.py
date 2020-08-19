def push(st, val):
    st.append(val)

def pop(st):
    if len(st) == 0:
        return None
    else:
        res = st[-1]
        del st[-1]
        return res

def checkBracket(strInp):
    stackList = []
    length = len(strInp)
    
    for i in range(0, length):
        if strInp[i] == "(":
            push(stackList, "(")
        else:
            p = pop(stackList)
            if p == None:
                return False
    
    return len(stackList) == 0
    
T = int(input())

for _ in range(0, T):
    if checkBracket(input()):
        print("YES")
    else:
        print("NO")