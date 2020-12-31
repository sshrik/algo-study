import sys
WALL = -21
EMPTY = -20

NOT_BREAK = 0
BREAK = 1

NOT_VISITED = 0
VISITED = 1

# 동서남북
dir_x = [0, 0, -1, 1]
dir_y = [1, -1, 0, 0]

def BFS_with_break(board, M, N):
    # (x, y, cnt, is_break)
    bfs_queue = []
    visited = [
        [[NOT_VISITED for _ in range(0, M)] for _ in range(0, N)], 
        [[NOT_VISITED for _ in range(0, M)] for _ in range(0, N)]
    ]   # visited[x][y][is_break]

    # 첫번째 칸은 (0, 0). (0, 0) 에서 시작하기.
    for d in range(0, 4):
        if is_in(board, N, M, dir_x[d], dir_y[d]):
            if is_wall(board, dir_x[d], dir_y[d]):
                bfs_queue.append((dir_x[d], dir_y[d], 1, BREAK))
                visited[dir_x[d]][dir_y[d]][BREAK] = VISITED
            else:
                bfs_queue.append((dir_x[d], dir_y[d], 1, NOT_BREAK))
                visited[dir_x[d]][dir_y[d]][NOT_BREAK] = VISITED

    while bfs_queue.length > 0:
        now = bfs_queue.pop()
        for d in range(0, 4):
            x = now[0] + dir_x[d]
            y = now[1] + dir_y[d]
            cnt = now[2] + 1
            is_break = now[3]

            if is_in(board, N, M, x, y):
                if is_wall(board, x, y):
                    if is_break != BREAK:
                        if visited[x][y][BREAK] == NOT_VISITED:
                            bfs_queue.append((x, y, cnt, BREAK))
                            visited[x][y][BREAK] = VISITED

    return -1

def is_in(board, N, M, x, y):
    return x >= 0 and x < N and y >= 0 and y < M

def is_wall(board, x, y):
    return board[x][y] == WALL

# For fast I / O.
if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])
    board = [[] for _ in range(0, N)]
    
    for i in range(0, N):
        inp = sys.stdin.readline().rstrip()
        for j in range(0, M):
            if inp[j] == '0':
                board.append(EMPTY)
            else:
                board.append(WALL)
    