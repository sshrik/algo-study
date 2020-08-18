import sys

EMPTY = 0
WALL = 1
VIRUS = 2

def check_safe_area(board, N, M, wall1, wall2, wall3):
    # check how many safe area in give boards.
    # For checking, copy given boards and set given 3 wall.
    copy_board = [[] for _ in range(0, N)]
    virus_queue = []

    for b_x in range(0, N):
        for b_y in range(0, M):
            if board[b_x][b_y] == VIRUS:
                virus_queue.append((b_x, b_y))
            copy_board[b_x].append(board[b_x][b_y])
    
    copy_board[wall1[0]][wall1[1]] = WALL
    copy_board[wall2[0]][wall2[1]] = WALL
    copy_board[wall3[0]][wall3[1]] = WALL

    # 바이러스 퍼뜨리기
    spread_virus(copy_board, N, M, virus_queue)

    return check_safe_area_number(copy_board, N, M), copy_board

def print_board(board, N, M):
    print("_________________________")
    for x in range(0, N):
        for y in range(0, M):
            if board[x][y] == EMPTY:
                print(" ", end="")
            elif board[x][y] == WALL:
                print("#", end="")
            else:
                print("*", end="")
        print("")

def check_safe_area_number(board, N, M):
    # Check safe area number given board.
    safe_number = 0

    for x in range(0, N):
        for y in range(0, M):
            if board[x][y] == EMPTY:
                safe_number += 1

    return safe_number

def spread_virus(board, N, M, virus_queue):
    while len(virus_queue) != 0:
        x = virus_queue[0][0]
        y = virus_queue[0][1]

        # Set 4-way with virus if exist and not WALL
        if set_virus(board, N, M, x + 1, y):
            virus_queue.append((x + 1, y))
        if set_virus(board, N, M, x - 1, y):
            virus_queue.append((x - 1, y))
        if set_virus(board, N, M, x, y + 1):
            virus_queue.append((x, y + 1))
        if set_virus(board, N, M, x, y - 1):
            virus_queue.append((x, y - 1))
        
        del virus_queue[0]

def set_virus(board, N, M, x, y):
    if 0 <= x and x < N and 0 <= y and y < M:
        if board[x][y] == EMPTY:
            board[x][y] = VIRUS
            return True
    return False

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])
    
    empty_list = []
    board = [[] for _ in range(0, N)]

    for n in range(0, N):
        inp = sys.stdin.readline().rstrip().split(" ")
        for m in range(0, M):
            board[n].append(int(inp[m]))
            if int(inp[m]) == 0:
                empty_list.append((n, m))

    max_safe_number = -1
    empty_size = len(empty_list)

    # 비어있는 곳 리스트 중에서 무작위로 3개를 고른다음 안전한 곳의 크기를 구한다.
    for i in range(0, empty_size - 2):
        for j in range(i + 1, empty_size - 1):
            for k in range(j + 1, empty_size):
                safe_number, max_board = check_safe_area(board, N, M, empty_list[i], empty_list[j], empty_list[k])
                if max_safe_number < safe_number:
                    max_safe_number = safe_number
                    # print_board(max_board, N, M)
    
    print(max_safe_number)

'''
6 6
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 0 0 1
0 0 0 0 0 1
0 0 0 0 0 1
0 0 2 2 0 0

6 6
0 0 0 0 0 0
2 0 0 0 0 2
1 1 0 0 0 1
0 0 0 0 0 1
0 0 0 0 0 1
0 0 0 0 0 0

3 3
0 0 0
0 2 0
0 0 0
'''