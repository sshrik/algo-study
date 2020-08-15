def binSearch(arr, want):
    # Binary Search with non-recursive - and return index.
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
            return midIndx
        length = end - start + 1
        
    if parseArr[start] == want:
        return start
    elif parseArr[end] == want:
        return end
    else:
        return -1

N = int(input())
n = []
nNum = []
inp = input().split(" ")

n.append(int(inp[0]))
nNum.append(1)
insertFlag = True

for i in range(1, N):
    nx = int(inp[i])
    for j in range(0, len(n)):
        if n[j] > nx:
            if n[j - 1] == nx:
                insertFlag = False
                nNum[j - 1] += 1
                break
            else:
                insertFlag = False
                n.insert(j, nx)
                nNum.insert(j, 1)
                break
    if insertFlag:
        if n[j] == nx:
            nNum[j] += 1
        else:
            n.append(nx)
            nNum.append(1)
    else:
        insertFlag = True

M = int(input())
inp = input().split(" ")

for i in range(0, M):
    w = int(inp[i])
    indx = binSearch(n, w)
    if indx == -1:
        print("0", end=" ")
    else:
        print(nNum[indx], end=" ")