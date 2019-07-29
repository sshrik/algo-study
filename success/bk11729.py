def printHanoi(N, cur, mid, dest):
    if N == 1:
        print("1 3")
    elif N == 2:
        print(str(cur) + " " + str(mid))
        print(str(cur) + " " + str(dest))
        print(str(mid) + " " + str(dest))
    else:
        printHanoi(N - 1, cur, dest, mid)
        print(str(cur) + " " + str(dest))
        printHanoi(N - 1, mid, cur, dest)

def countHanoi(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        return countHanoi(N - 1) + 1 + countHanoi(N - 1)

N = int(input())
print(countHanoi(N))
printHanoi(N, 1, 2, 3)
