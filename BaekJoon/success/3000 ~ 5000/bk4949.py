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
        # Check small bracket.
        if strInp[i] == "(":
            push(stackList, "(")
        elif strInp[i] == ")":
            p = pop(stackList)
            if p != "(" or p == None:
                return False
        # Check Large bracket.
        elif strInp[i] == "[":
            push(stackList, "[")
        elif strInp[i] == "]":
            p = pop(stackList)
            if p != "[" or p == None:
                return False
        
    return len(stackList) == 0
    
# If endFlag Flase, end.
endFlag = True
while endFlag:
    inp = input()
    cumInp = ""
    
    if inp == ".":
        endFlag = False
    elif inp.endswith("."):
        cumInp += inp
        if checkBracket(cumInp):
            print("yes")
        else:
            print("no")
        cumInp = ""
    else:
        cumInp += inp
    