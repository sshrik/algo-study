# https://www.acmicpc.net/problem/16953
import sys
fastio = sys.stdin.readline

from collections import deque

def makeB(A, B):
    bfsQueue = deque([(A, 0)])
    while bfsQueue:
        now = bfsQueue.popleft()
        nowNum = now[0]
        nowStep = now[1]

        if nowNum > B:
            continue
        elif nowNum == B:
            return nowStep + 1
        
        bfsQueue.append((nowNum * 2, nowStep + 1))
        bfsQueue.append((nowNum * 10 + 1, nowStep + 1))

    return -1


if __name__ == "__main__":
    inp = fastio().split(" ")
    A = int(inp[0])
    B = int(inp[1])

    print(makeB(A, B))