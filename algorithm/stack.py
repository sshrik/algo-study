def push(st, val):
    st.append(val)

def pop(st):
    if len(st) == 0:
        return None
    else:
        res = st[-1]
        del st[-1]
        return res