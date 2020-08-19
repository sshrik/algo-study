import collections

def getJoshepususNum(q, K):
    q.rotate(K * -1)
    return q.pop()

if __name__ == "__main__":
    inp = input().split(" ")
    N = int(inp[0])
    K = int(inp[1])
    person = collections.deque(range(1, N + 1))
    joshepususList = []

    while len(person) != 0 :
        num = getJoshepususNum(person, K)
        joshepususList.append(num)
    
    print("<", end="")
    for i in range(0, N - 1):
        print(joshepususList[i], end=", ")
    print(str(joshepususList[N - 1]) + ">", end="")
