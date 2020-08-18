import sys

QUEEN = 1
EMPTY = 0

def possible(exist_x, exist_y, exist_down_diag, exist_up_diag, x, y):
    # N x N board[x][y]에 Queen을 놓았을 때 가능한지 체크
    if exist_x[x]:
        return False
    if exist_y[y]:
        return False
    if exist_down_diag[(x - y) + N - 1]:
        return False
    if exist_up_diag[(x + y)]:
        return False
    return True    

def check_next_queen(exist_x, exist_y, exist_down_diag, exist_up_diag, N, x, stack):
    if x == N:
        # print(stack)
        return 1
    else:
        cnt = 0
        for y in range(0, N):
            if possible(exist_x, exist_y, exist_down_diag, exist_up_diag, x, y):
                # Do not use board 2 x 2, then using True-False lists.
                exist_x[x] = True
                exist_y[y] = True
                exist_down_diag[(x - y) + N - 1] = True
                exist_up_diag[(x + y)] = True
                # stack.append((x, y))
                cnt += check_next_queen(exist_x, exist_y, exist_down_diag, exist_up_diag, N, x + 1, stack)
                # del stack[-1]
                exist_x[x] = False
                exist_y[y] = False
                exist_down_diag[(x - y) + N - 1] = False
                exist_up_diag[(x + y)] = False
        return cnt

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    N = int(sys.stdin.readline().rstrip())
    
    if N == 1:
        print(1)
    elif N == 2 or N == 3:
        print(0)
    else:
        board = [[EMPTY for _ in range(0, N)] for _ in range(0, N)]
        stack = []
        exist_x = [False for _ in range(0, N)] 
        exist_y = [False for _ in range(0, N)] 
        exist_down_diag  = [False for _ in range(0, 2 * N - 1)]
        exist_up_diag = [False for _ in range(0, 2 * N - 1)] 
        print(check_next_queen(exist_x, exist_y, exist_down_diag, exist_up_diag, N, 0, stack))
