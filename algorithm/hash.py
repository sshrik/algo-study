def getHashKey(value, sumRes):
    if value > sumRes:
        return None
    else :
        return sumRes - value

def getHashValue(key, arr):
    # Return Hash value which have given key.
    return arr[key]

def makeHashTable(inp, sumRes):
    # Make sumRes + 1 length empty lists list.
    arr = list([].append( [] for _ in range(0, sumRes + 1) ))
    for i in range(0, len(inp)):
        key = getHashKey(inp[i], sumRes)
        if key != None:
            arr[key].append(i) # If collision occured, append can act like seperate chaining rule.
    return arr