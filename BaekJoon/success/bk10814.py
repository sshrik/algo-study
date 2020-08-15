def compBigger(arr1, arr2):
    # Return True if arr1 is bigger.
    if arr1[0] > arr2[0]:
        return True
    elif arr1[0] < arr2[0]:
        return False
    else:
        if arr1[2] > arr2[2]:
            return True
        else:
            return False


def merge(arr1, arr2):
    res = []
    i = 0
    j = 0
    while i != len(arr1) and j != len(arr2):
        if compBigger(arr1[i], arr2[j]):
            res.append(arr2[j])
            j += 1
        else:
            res.append(arr1[i])
            i += 1
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

N = int(input())

person = []

for i in range(0, N):
    inp = input().split(" ")
    person.append([int(inp[0]), inp[1], i])

person = mergeNonRecusive(person)

for i in range(0, N):
    print(str(person[i][0]) + " " + person[i][1])