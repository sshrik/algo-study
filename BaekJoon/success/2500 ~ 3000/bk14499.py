# https://www.acmicpc.net/problem/14499
import sys

class Dice:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
        self.back = 0
        self.front = 0
    
    def move(self, direction):
        if direction == 0:
            temp = self.right
            self.right = self.top
            self.top = self.left
            self.left = self.bottom
            self.bottom = temp
        elif direction == 1:
            temp = self.top
            self.top = self.right
            self.right = self.bottom
            self.bottom = self.left
            self.left = temp
        elif direction == 2:
            temp = self.top
            self.top = self.front
            self.front = self.bottom
            self.bottom = self.back
            self.back = temp
        else:
            temp = self.front
            self.front = self.top
            self.top = self.back
            self.back = self.bottom
            self.bottom = temp
        return self.bottom

# 동 서 북 남
dir_x = [0, 0, -1, 1]
dir_y = [1, -1, 0, 0]

def can_go(N, M, x, y, direction):
    return 0 <= x + dir_x[direction] < N and 0 <= y + dir_y[direction] < M

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])
    x = int(inp[2])
    y = int(inp[3])
    K = int(inp[4])
    dice = Dice()
    
    number_map = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        inp = sys.stdin.readline().rstrip().split(" ")
        for j in range(M):
            number_map[i][j] = int(inp[j])

    moving = sys.stdin.readline().rstrip().split(" ")
    for k in range(K):
        direction = int(moving[k]) - 1
        if can_go(N, M, x, y, direction):
            dice.move(direction)
            x += dir_x[direction]
            y += dir_y[direction]
            if number_map[x][y] == 0:
                number_map[x][y] = dice.bottom
            else:
                dice.bottom = number_map[x][y]
                number_map[x][y] = 0
            print(dice.top)
        