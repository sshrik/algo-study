def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return int(a / b)

def doNextFunc(numList, nowLevel, remainList, result, small, large):
    # Recursive end, renewal small and large value.
    if nowLevel == len(numList):
        if result < small:
            small = result 
        if result > large:
            large = result 
        return small, large

    # For all operator, do function if operator count is remain.
    for i in range(0, 4):
        if remainList[i] > 0:
            # Count remain operator number.
            remainList[i] -= 1
            small, large = doNextFunc(numList, nowLevel + 1, remainList, funcList[i](result, numList[nowLevel]), small, large)
            remainList[i] += 1
    return small, large

if __name__ == "__main__":
    funcList = [add, sub, mul, div]
    # small and large number was given.
    small = 1000000001
    large = -1000000001
    N = int(input())

    # Make Number sequence.
    inp = input().split(" ")
    numList = []
    for i in range(0, N):
        numList.append(int(inp[i]))

    # Make operator remain sequence.
    inp = input().split(" ")
    remainList = []
    for i in range(0, 4):
        remainList.append(int(inp[i]))

    small, large = doNextFunc(numList, 1, remainList, numList[0], small, large)
    print(large)
    print(small)