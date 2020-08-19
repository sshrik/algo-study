import sys

# @ : 시작 위치
# # : tetromino 위치

# @###
def tetro0(board, x, y, N, M):
    add_all = 0

    if is_in(board, x, y, N, M) and is_in(board, x, y + 1, N, M) and is_in(board, x, y + 2, N, M) and is_in(board, x, y + 3, N, M):
        add_all = board[x][y] + board[x][y + 1] + board[x][y + 2] + board[x][y + 3]

    return add_all
    
# @##
#   #
def tetro1(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x, y + 1, N, M) and is_in(board, x, y + 2, N, M) and is_in(board, x + 1, y + 2, N, M):
        add_all = board[x][y] + board[x][y + 1] + board[x][y + 2] + board[x + 1][y + 2]

    return add_all

#   #
# @##
def tetro2(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x, y + 1, N, M) and is_in(board, x, y + 2, N, M) and is_in(board, x - 1, y + 2, N, M):
        add_all = board[x][y] + board[x][y + 1] + board[x][y + 2] + board[x - 1][y + 2]

    return add_all
    
# @##
#  #
def tetro3(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x, y + 1, N, M) and is_in(board, x, y + 2, N, M) and is_in(board, x + 1, y + 1, N, M):
        add_all = board[x][y] + board[x][y + 1] + board[x][y + 2] + board[x + 1][y + 1]

    return add_all
    
#  #
# @##
def tetro4(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x, y + 1, N, M) and is_in(board, x, y + 2, N, M) and is_in(board, x - 1, y + 1, N, M):
        add_all = board[x][y] + board[x][y + 1] + board[x][y + 2] + board[x - 1][y + 1]

    return add_all
    
# @##
# #
def tetro5(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x, y + 1, N, M) and is_in(board, x, y + 2, N, M) and is_in(board, x + 1, y, N, M):
        add_all = board[x][y] + board[x][y + 1] + board[x][y + 2] + board[x + 1][y]

    return add_all

# #
# @##
def tetro6(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x, y + 1, N, M) and is_in(board, x, y + 2, N, M) and is_in(board, x - 1, y, N, M):
        add_all = board[x][y] + board[x][y + 1] + board[x][y + 2] + board[x - 1][y]

    return add_all
    
# @#
# ##
def tetro7(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x, y + 1, N, M) and is_in(board, x + 1, y, N, M) and is_in(board, x + 1, y + 1, N, M):
        add_all = board[x][y] + board[x][y + 1] + board[x + 1][y] + board[x + 1][y + 1]

    return add_all
    
# @#
#  ##
def tetro8(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x, y + 1, N, M) and is_in(board, x + 1, y + 1, N, M) and is_in(board, x + 1, y + 2, N, M):
        add_all = board[x][y] + board[x][y + 1] + board[x + 1][y + 1] + board[x + 1][y + 2]

    return add_all
    
#  @#
# ##
def tetro9(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x, y + 1, N, M) and is_in(board, x + 1, y - 1, N, M) and is_in(board, x + 1, y, N, M) :
        add_all = board[x][y] + board[x][y + 1] + board[x + 1][y - 1] + board[x + 1][y]

    return add_all

# @### 세로로
def tetro10(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x + 1, y, N, M) and is_in(board, x + 2, y, N, M) and is_in(board, x + 3, y, N, M) :
        add_all = board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x + 3][y]

    return add_all

#  @
#  #
# ##
def tetro11(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x + 1, y, N, M) and is_in(board, x + 2, y, N, M) and is_in(board, x + 2, y - 1, N, M) :
        add_all = board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x + 2][y - 1]

    return add_all

# @
# #
# ##
def tetro12(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x + 1, y, N, M) and is_in(board, x + 2, y, N, M) and is_in(board, x + 2, y + 1, N, M) :
        add_all = board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x + 2][y + 1]

    return add_all

#  @
# ##
#  #
def tetro13(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x + 1, y, N, M) and is_in(board, x + 2, y, N, M) and is_in(board, x + 1, y - 1, N, M) :
        add_all = board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x + 1][y - 1]

    return add_all

# @
# ##
# #
def tetro14(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x + 1, y, N, M) and is_in(board, x + 2, y, N, M) and is_in(board, x + 1, y + 1, N, M) :
        add_all = board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x + 1][y + 1]

    return add_all

# @#
# #
# #
def tetro15(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x + 1, y, N, M) and is_in(board, x + 2, y, N, M) and is_in(board, x, y + 1, N, M) :
        add_all = board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x][y + 1]

    return add_all

# #@
#  #
#  #
def tetro16(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x + 1, y, N, M) and is_in(board, x + 2, y, N, M) and is_in(board, x, y - 1, N, M) :
        add_all = board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x][y - 1]

    return add_all

#  @
# ##
# #
def tetro17(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x + 1, y, N, M) and is_in(board, x + 1, y - 1, N, M) and is_in(board, x + 2, y - 1, N, M) :
        add_all = board[x][y] + board[x + 1][y] + board[x + 1][y - 1] + board[x + 2][y - 1]

    return add_all

# @
# ##
#  #
def tetro18(board, x, y, N, M):
    add_all = 0
    
    if is_in(board, x, y, N, M) and is_in(board, x + 1, y, N, M) and is_in(board, x + 1, y + 1, N, M) and is_in(board, x + 2, y + 1, N, M) :
        add_all = board[x][y] + board[x + 1][y] + board[x + 1][y + 1] + board[x + 2][y + 1]

    return add_all

def is_in(board, x, y, N, M):
    if -1 < x and x < N:
        if -1 < y and y < M:
            return True
    return False

tetro_func = [tetro0, tetro1, tetro2, tetro3, tetro4, tetro5, tetro6, tetro7, tetro8, tetro9, tetro10, tetro11, tetro12, tetro13, tetro14, tetro15, tetro16, tetro17, tetro18]

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])
    board = [[] for _ in range(0, N)]

    for x in range(0, N):
        inp = sys.stdin.readline().rstrip().split(" ")
        for board_content in inp:
            board[x].append(int(board_content))
    
    max_add = 0
    for x in range(0, N):
        for y in range(0, M):
            for tetroN in tetro_func:
                add_all = tetroN(board,x, y, N, M)
                if max_add < add_all:
                    # print("( " + str(x) + ", " + str(y) + ") : " + str(tetroN))
                    max_add = add_all
    print(max_add)
    