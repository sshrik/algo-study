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

N = int(input())

# Get A list and sorting.
A = []
inp = input().split(" ")

for i in range(0, N):
    A.append(int(inp[i]))

A.sort()

M = int(input())
# W : wanted list.
W = input().split(" ")

for i in range(0, M):
    if binSearchNonRecursiveNonSlicing(A, int(W[i])):
        print("1")
    else:
        print("0")