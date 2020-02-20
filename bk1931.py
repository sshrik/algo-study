def canPicked(startTime, takingTime, pickedList, pickCandidate):
    for i in range(0, len(pickedList)):
        if startTime[pickedList[i]] < startTime[pickCandidate] < startTime[pickedList[i]] + takingTime[pickedList[i]]:
            return False
        elif startTime[pickCandidate] < startTime[pickedList[i]] < startTime[pickCandidate] + takingTime[pickCandidate]:
            return False
        elif startTime[pickedList[i]] < startTime[pickCandidate] + takingTime[pickCandidate] < startTime[pickedList[i]] + takingTime[pickedList[i]]:
            return False
        elif startTime[pickCandidate] < startTime[pickedList[i]] + takingTime[pickedList[i]] < startTime[pickCandidate] + takingTime[pickCandidate]:
            return False
    return True


if __name__ == "__main__":
    n = int(input())
    startTime = []
    takingTime = []
    j = 0

    for i in range(0, n):
        inp = input().split(" ")
        start = int(inp[0])
        taking = int(inp[1]) - int(inp[0])
        addFlag = False
        # Count from front to sort with taking time.
        for j in range(0, i):
            if takingTime[j] == taking:
                if startTime[j] >= start:
                    startTime.insert(j, start)
                    takingTime.insert(j, taking)
                    addFlag = True
                    break
            elif takingTime[j] > taking:
                startTime.insert(j, start)
                takingTime.insert(j, taking)
                addFlag = True
                break
        if not addFlag:
            startTime.append(start)
            takingTime.append(taking)

    
    # print(startTime)
    # print(takingTime)

    picked = 0
    pickedList = []
    for i in range(0, n):
        if canPicked(startTime, takingTime, pickedList, i):
            # pickedList.append(i)
            picked += 1
    # for i in pickedList:
        # print(str(startTime[i]) + " ~ " + str(startTime[i] + takingTime[i]))
    print(picked)