import sys
from collections import deque

import heapq

fastio = sys.stdin.readline

if __name__ == "__main__":
    T = int(fastio())

    for t in range(T):
        priority = []
        realQueue = deque()
        splitLine = fastio().split(" ")
        N = int(splitLine[0])
        M = int(splitLine[1])

        splitLine = fastio().split(" ")
        dest = int(splitLine[M])

        for i in range(N):
            realQueue.append((int(splitLine[i]), i))
            heapq.heappush(priority, int(splitLine[i]) * -1)

        i = 0
        endFlag = False
        while realQueue and not endFlag:
            nowPriority = heapq.heappop(priority) * -1
            while True:
                nowEntry = realQueue.popleft()
                if nowEntry[0] == dest and nowEntry[1] == M and nowPriority == nowEntry[0]:
                    print(i + 1)
                    endFlag = True
                    break
                elif nowEntry[0] == nowPriority:
                    i += 1
                    break
                else:
                    realQueue.append(nowEntry)

