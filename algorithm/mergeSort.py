def mergeSort(arr):
    # If arr length 0, 1 return sorted.
    if len(arr) == 1 or len(arr) == 0:
        return arr
    # Else, merge it to front and back ( with sorted ) and merge it.
    length = int(len(arr) / 2)
    return merge(mergeSort(arr[0:length]), mergeSort(arr[length:]))

def merge(arr1, arr2):
    res = []
    i = 0
    j = 0
    while i != len(arr1) and j != len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res = res + arr1[i:] if j == len(arr2) else res + arr2[j:]
    return res

def mergeNonRecusive(arr):
    # Parsing mean parse "arr" with length 1 or 0( which mean nothing. )
    parsedList = [[arr[i]] for i in range(0, len(arr))]
    
    # Merge parsed list to one list.
    while len(parsedList) != 1:
        # Merge all parsed list which have pair.
        tempList = [ merge(parsedList[2 * i], parsedList[2 * i + 1]) for i in range(0, int(len(parsedList) / 2)) ]
        tempList = tempList + [parsedList[-1]] if len(parsedList) % 2 == 1 else tempList
        parsedList = tempList
    
    # parsedList has list values.
    return parsedList[0]

def compBigger(arr1, arr2):
    # Return True if arr1 is bigger
    if arr1 > arr2:
        return True
    else:
        return False

def mergeNonRecusiveAndFunction(arr, func="default"):
    # If given function not defined...
    if func=="default":
        return mergeNonRecusive(arr)

    # Parsing mean parse "arr" with length 1 or 0( which mean nothing. )
    parsedList = [[arr[i]] for i in range(0, len(arr))]
    # Merge parsed list to one list.
    while len(parsedList) != 1:
        # Merge all parsed list which have pair.
        tempList = [ merge(parsedList[2 * i], parsedList[2 * i + 1]) for i in range(0, int(len(parsedList) / 2)) ]
        tempList = tempList + [parsedList[-1]] if len(parsedList) % 2 == 1 else tempList
        parsedList = tempList
    
    # parsedList has list values.
    return parsedList[0]
    
inpArr = [2,5,6,1,72,10,2,5,6,1,2,45,21,230]
res1 = mergeNonRecusive(inpArr)
res2 = mergeSort(inpArr)
print(sorted(inpArr))
print(res1)
print(res2)