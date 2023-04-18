# https://www.acmicpc.net/problem/2146
import sys
from heapq import heappush, heappop

fastio = sys.stdin.readline

LAND = 1
WATER = 0

VISITED = 1
NOT_VISITED = 0

EAST = 0
WEST = 1
SOUTH = 2
NORTH = 3

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def canGo(direction, N, i, j):
  if direction == EAST:
    return j + 1 < N
  if direction == WEST:
    return j - 1 >= 0
  if direction == SOUTH:
    return i + 1 < N
  if direction == NORTH:
    return i - 1 >= 0

def printBoard(board):
  for i in range(len(board)):
    for j in range(len(board)):
      print(board[i][j], end=" ")
    print()
    

def getShortestBridge(board, i, j, mapBoard, nowLand):
  queue = []
  heappush(queue, [0, i, j])
  
  distanceMap = [[0 for _ in range(N)] for _ in range(N)]
  visited = [[False for _ in range(N)] for _ in range(N)]
  
  while len(queue) > 0:
    [_, nowX, nowY] = queue.pop(0)
    
    if visited[nowX][nowY]:
      continue
    
    visited[nowX][nowY] = True
    
    for direction in range(4):
      if canGo(direction, N, nowX, nowY):
        nextX = nowX + dx[direction]
        nextY = nowY + dy[direction]

        if visited[nextX][nextY]:
          continue

        if board[nowX][nowY] == LAND:
          if board[nextX][nextY] == LAND and mapBoard[nextX][nextY] == nowLand:
            heappush(queue, [distanceMap[nowX][nowY], nextX, nextY])
          elif board[nextX][nextY] == WATER:
            distanceMap[nextX][nextY] = distanceMap[nowX][nowY] + 1
            heappush(queue, [distanceMap[nowX][nowY], nextX, nextY])
        elif board[nowX][nowY] == WATER:
          if board[nextX][nextY] == LAND:
            if mapBoard[nextX][nextY] != nowLand:
              return distanceMap[nowX][nowY]
            else:
              heappush(queue, [distanceMap[nowX][nowY], nextX, nextY])
          elif board[nextX][nextY] == WATER:
            distanceMap[nextX][nextY] = distanceMap[nowX][nowY] + 1
            heappush(queue, [distanceMap[nowX][nowY], nextX, nextY])
            
def searchLand(board, mapBoard, i, j, nowLand):
  queue = [[i, j]]
  
  while len(queue) > 0:
    [nowX, nowY] = queue.pop()
    
    if mapBoard[nowX][nowY] == NOT_VISITED and board[nowX][nowY] == LAND:
      mapBoard[nowX][nowY] = nowLand
    else:
      continue
     
    for direction in range(4):
      if canGo(direction, N, nowX, nowY):
        nextX = nowX + dx[direction]
        nextY = nowY + dy[direction]
        
        if mapBoard[nextX][nextY] == NOT_VISITED and board[nextX][nextY] == LAND:
          queue.append([nextX, nextY])

if __name__ == "__main__":
  N = int(fastio())
  board = [list(map(int, fastio().split(" "))) for _ in range(N)]
  mapBoard = [[NOT_VISITED for _ in range(N)] for _ in range(N)]
  
  minValue = 100 * 100 + 1
  
  nowLand = 1
  
  for i in range(N):
    for j in range(N):
      if board[i][j] == LAND and mapBoard[i][j] == NOT_VISITED:
        searchLand(board, mapBoard, i, j, nowLand)
        bridgeLength = getShortestBridge(board, i, j, mapBoard, nowLand)
        
        nowLand += 1
        if bridgeLength < minValue:
          minValue = bridgeLength
  
print(minValue)
