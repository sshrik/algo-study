def binSearch(arr, want):
    # Check recursive depth outer
    if len(arr) == 1:
        return arr[0] == want
    else:
        midIndx = int(len(arr)/2)

    if arr[midIndx] < want:
        return binSearch(arr[midIndx:], want)
    elif arr[midIndx] > want:
        return binSearch(arr[0:midIndx], want)
    else:
        return True

def binSearchNonRecursive(arr, want):
    parseArr = arr

    while len(parseArr) != 1:
        midIndx = int(len(parseArr)/2)
        if parseArr[midIndx] < want:
            parseArr = parseArr[midIndx:]
        elif parseArr[midIndx] > want:
            parseArr = parseArr[0:midIndx]
        else:
            return True
        
    return parseArr[0] == want

def binSearchNonRecursiveNonSlicing(arr, want):
    # Binary Search with non-recursive.
    parseArr = arr
    length = len(parseArr)
    # set start and end index.
    start = 0
    end = length - 1
    midIndx = -1

    while length != 2:
        # set mid value and check with want value.
        midIndx = start + int(length/2)
        if parseArr[midIndx] < want:
            start = midIndx
        elif parseArr[midIndx] > want:
            end = midIndx
        else:
            return True
        length = end - start + 1
        
    return parseArr[start] == want or parseArr[end] == want

print(binSearchNonRecursiveNonSlicing([2,5,7,8,9,20,21,24], 5))