def push(st, val):
    st.append(val)

def pop(st):
    res = st[-1]
    del st[-1]
    return res

K = int(input())

stackList = []
addUp = 0

for _ in range(0, K):
    inp = int(input())
    if inp == 0:
        addUp -= pop(stackList)
    else:
        push(stackList, inp)
        addUp += inp

print(addUp)