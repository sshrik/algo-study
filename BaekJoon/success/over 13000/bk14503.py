import sys

WALL = 1
EMPTY = 0
DIRTY = 0
CLEAN = -1

EAST = 1
WEST = 3
SOUTH = 2
NORTH = 0

def get_back_dir_indx(direction):
    # 각 방향에 따른 뒤쪽의 indx 설정
    x_indx = 0
    y_indx = 0

    if direction == EAST:
        y_indx = -1
    elif direction == WEST:
        y_indx = 1
    elif direction == SOUTH:
        x_indx = -1
    elif direction == NORTH:
        x_indx = 1
    
    return x_indx, y_indx

def get_left_dir_indx(direction):
    # 각 방향에 따른 왼쪽의 indx.
    x_indx = 0
    y_indx = 0

    if direction == EAST:
        x_indx = -1
    elif direction == WEST:
        x_indx = 1
    elif direction == SOUTH:
        y_indx = 1
    elif direction == NORTH:
        y_indx = -1

    return x_indx, y_indx

def check_4_way_cleanable(room, N, M, x, y):
    # 사방이 청소 되어있거나 벽이면 return True
    end_flag = True
    
    # 사방이 청소되어 있거나 벽인지 확인.
    if not is_endable(room, N, M, x - 1, y):
        end_flag = False
    elif not is_endable(room, N, M, x + 1, y):
        end_flag = False
    elif not is_endable(room, N, M, x, y - 1):
        end_flag = False
    elif not is_endable(room, N, M, x, y + 1):
        end_flag = False

    return end_flag

def is_wall(room, N, M, x, y):
    if x != N and x != -1:
        if y != M and y != -1:
            return room[x][y] == WALL
    return True

def is_clean(room, N, M, x, y):
    if x != N and x != -1:
        if y != M and y != -1:
            return room[x][y] == CLEAN
    return True

def is_endable(room, N, M, x, y):
    if x != N and x != -1:
        if y != M and y != -1:
            return room[x][y] == CLEAN or room[x][y] == WALL
    return True

def turn_left(direction):
    dir_list = [EAST, NORTH, WEST, SOUTH]
    idx = dir_list.index(direction)
    if idx == len(dir_list) - 1:
        return dir_list[0]
    else:
        return dir_list[idx + 1]

def print_room(room, N, M, x, y, direction):
    print("____________________________")
    for n in range(0, N):
        for m in range(0, M):
            if n == x and m == y:
                if direction == EAST:
                    print(">", end="")
                if direction == WEST:
                    print("<", end="")
                if direction == SOUTH:
                    print("v", end="")
                if direction == NORTH:
                    print("^", end="")
            elif room[n][m] == WALL:
                print("#", end="")
            elif room[n][m] == CLEAN:
                print("_", end="")
            elif room[n][m] == DIRTY:
                print("%", end="")
        print(" ", end="")
        for m in range(0, M):
            if room[n][m] == WALL:
                print("#", end="")
            elif room[n][m] == CLEAN:
                print("_", end="")
            elif room[n][m] == DIRTY:
                print("%", end="")
        print("")

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])

    inp = sys.stdin.readline().rstrip().split(" ")
    r = int(inp[0])
    c = int(inp[1])
    direction = int(inp[2])

    room = [[] for _ in range(0, N)]
    for x in range(0, N):
        inp = sys.stdin.readline().rstrip().split(" ")
        for room_contents in inp:
            room[x].append(int(room_contents))

    clean_cnt = 0
    # print_room(room, N, M, r, c, direction)
    while True:
        # print("( " + str(r) + ", " + str(c) + " ) : " + str(is_clean(room, N, M, r, c)) + " and direction : " + str(direction))
        # print_room(room, N, M, r, c, direction)
        # input("")
        no_2_pass_flag = False
        no_1_pass_flag = False
        # 현재 자리가 더러우면 치우고 시작한다. ( - 1 - )
        if not is_clean(room, N, M, r, c) and not no_1_pass_flag:
            room[r][c] = CLEAN
            clean_cnt += 1
        
        # 왼쪽 방향으로 회전하면서 확인한다. ( - 2 - )
        for _ in range(0, 4):
            x_indx, y_indx = get_left_dir_indx(direction)
            if not is_clean(room, N, M, r + x_indx, c + y_indx) and not is_wall(room, N, M, r + x_indx, c + y_indx):
                # 아직 청소하지 않은 공간이 있다면 회전 후 1칸 전진. 그 후, 1번 진행.
                direction = turn_left(direction)
                r = r + x_indx
                c = c + y_indx
                no_2_pass_flag = True
                no_1_pass_flag = False
                break
            else:
                # 청소할 공간이 없다면 다시 회전. 2로 돌아감
                direction = turn_left(direction)

        # 청소하지 않은 공간이 있기 때문에 1로 진행.
        if no_2_pass_flag:
            continue
        else:
            # 사방이 청소 되어있거나 벽일 때, ( 2 - c, d )
            if check_4_way_cleanable(room, N, M, r, c):
                # 뒤가 벽이면 끝 ( 2 - d )
                x_indx, y_indx = get_back_dir_indx(direction)
                if is_wall(room, N, M, r + x_indx, c + y_indx):
                    break
                else:
                    # 아니면 한칸 후진 후 2번으로 돌아감.
                    no_1_pass_flag = True
                    r = r + x_indx
                    c = c + y_indx
    print(clean_cnt)
    


'''
3 5
1 2 1
1 1 1 1 1
1 0 0 0 1
1 1 1 1 1

= 3

3 3
1 1 0
1 1 1
1 0 1
1 1 1
1

11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

= 57

5 3
1 1 0
1 1 1
1 0 1
1 0 1
1 0 1
1 1 1

= 3

4 6
2 3 0
1 1 1 1 1 1
1 0 0 1 0 1
1 0 0 0 0 1
1 1 1 1 1 1

= 5

10 10
1 1 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

= 64

10 10
1 1 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 0 1 1 1 1 1 1 1 1
1 0 1 0 0 0 0 1 0 1
1 0 1 0 0 0 1 0 0 1
1 0 1 0 1 1 1 0 1 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

= 32

6 6
1 1 0
1 1 1 1 1 1
1 0 0 1 0 1
1 1 0 0 0 1
1 1 0 1 1 1
1 0 0 0 0 1
1 1 1 1 1 1

= 6


'''