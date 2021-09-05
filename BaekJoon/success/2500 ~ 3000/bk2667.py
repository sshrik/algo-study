# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
fastio = sys.stdin.readline

dirX = [1, -1, 0, 0]
dirY = [0, 0, 1, -1]

EMPTY = 0

def canGo(width, height, x, y, dir) :
    return 0 <= x + dirX[dir] < width and 0 <= y + dirY[dir] < height

def bfs(apartMap, visited, width, height, startX=0, startY=0):
    x = startX
    y = startY
    startNode = apartMap[y][x]
    dfsStack = deque([(x, y)])

    num = 0
    while dfsStack:
        now = dfsStack.pop()
        nowX = now[0]
        nowY = now[1]
        if visited[nowY][nowX]:
            continue
        visited[nowY][nowX] = True
        num += 1
        for d in range(4):
            if canGo(width, height, nowX, nowY, d) and apartMap[nowY + dirY[d]][nowX + dirX[d]] == startNode:
                dfsStack.append((nowX + dirX[d], nowY + dirY[d]))
    return num    


if __name__ == "__main__":
    N = int(fastio().rstrip())

    apartMap = []
    for _ in range(N):
        apartMapNum = fastio().rstrip()
        apartMap.append([int(i) for i in apartMapNum])
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    apartCount = []

    for i in range(N):
        for j in range(N):
            if not visited[j][i] and apartMap[j][i] != EMPTY:
                apartCount.append(bfs(apartMap, visited, N, N, i, j))
    print(len(apartCount))
    apartCount.sort()

    for ac in apartCount:
        print(ac)









