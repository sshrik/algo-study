# https://www.acmicpc.net/problem/15683
# 실수 1 : 해당 CCTV 부터 출발하면서 벽이 있는지 보아야 했는데, 0 부터 출발하면서 봐서 에러가 났었다.

import sys
from copy import deepcopy

# Map[x][y]
dir_x = [0, 0 -1, 1]
dir_y = [1, -1, 0, 0]

rotation_info = [
    [],
    [0, 1, 2, 3],
    [0, 1],
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0]
]

EMPTY = 0
WALL = 6
WATCHING = -1

def set_watching_area(area, cctv_kind, cctv_x, cctv_y, rotation):
    if cctv_kind == 1:
        set_direction_area(area, cctv_x, cctv_y, rotation)
    elif cctv_kind == 2:
        if rotation == 0:
            set_direction_area(area, cctv_x, cctv_y, 0)
            set_direction_area(area, cctv_x, cctv_y, 1)
        else:
            set_direction_area(area, cctv_x, cctv_y, 2)
            set_direction_area(area, cctv_x, cctv_y, 3)
    elif cctv_kind == 3:
        if rotation == 0:
            set_direction_area(area, cctv_x, cctv_y, 0)
            set_direction_area(area, cctv_x, cctv_y, 3)
        elif rotation == 1:
            set_direction_area(area, cctv_x, cctv_y, 0)
            set_direction_area(area, cctv_x, cctv_y, 2)
        elif rotation == 2:
            set_direction_area(area, cctv_x, cctv_y, 1)
            set_direction_area(area, cctv_x, cctv_y, 2)
        elif rotation == 3:
            set_direction_area(area, cctv_x, cctv_y, 1)
            set_direction_area(area, cctv_x, cctv_y, 3)
    elif cctv_kind == 4:
        if rotation == 0:
            set_direction_area(area, cctv_x, cctv_y, 0)
            set_direction_area(area, cctv_x, cctv_y, 1)
            set_direction_area(area, cctv_x, cctv_y, 3)
        elif rotation == 1:
            set_direction_area(area, cctv_x, cctv_y, 0)
            set_direction_area(area, cctv_x, cctv_y, 2)
            set_direction_area(area, cctv_x, cctv_y, 3)
        elif rotation == 2:
            set_direction_area(area, cctv_x, cctv_y, 0)
            set_direction_area(area, cctv_x, cctv_y, 1)
            set_direction_area(area, cctv_x, cctv_y, 2)
        elif rotation == 3:
            set_direction_area(area, cctv_x, cctv_y, 1)
            set_direction_area(area, cctv_x, cctv_y, 2)
            set_direction_area(area, cctv_x, cctv_y, 3)
    elif cctv_kind == 5:
        for direction in range(0, 4):
            set_direction_area(area, cctv_x, cctv_y, direction)
    else:
        print("Error Occured. : SET WATCHING AREA cctv kind error.")

def set_direction_area(area, x, y, direction):
    max_x = len(area)
    max_y = len(area[0])

    if direction == 0:
        for i in range(y, max_y):
            if area[x][i] == EMPTY:
                area[x][i] = WATCHING
            elif area[x][i] == WALL:
                break
    elif direction == 1:
        for i in range(y, -1, -1):
            if area[x][i] == EMPTY:
                area[x][i] = WATCHING
            elif area[x][i] == WALL:
                break
    elif direction == 2:
        for i in range(x, max_x):
            if area[i][y] == EMPTY:
                area[i][y] = WATCHING
            elif area[i][y] == WALL:
                break
    elif direction == 3:
        for i in range(x, -1, -1):
            if area[i][y] == EMPTY:
                area[i][y] = WATCHING
            elif area[i][y] == WALL:
                break
    else:
        print("Error Occured : Direction not in 0 ~ 4.")

def count_empty_area(area):
    count = 0
    for area_arr in area:
        for a in area_arr:
            if a == EMPTY:
                count += 1
    return count

def print_map(area):
    for area_arr in area:
        for a in area_arr:
            if a == WALL:
                print("=", end="")
            elif a == WATCHING:
                print("%", end="")
            elif a == EMPTY:
                print("_", end="")
            else:
                print(a, end="")
        print("")

def count_backtracking(area, cctv_kind, cctv_loc_x, cctv_loc_y, cctv_index):
    if cctv_index == len(cctv_kind):
        #print_map(area)
        #print(count_empty_area(area))
        return count_empty_area(area)
    else:
        smallest_count = sys.maxsize
        for rot in rotation_info[cctv_kind[cctv_index]]:
            next_area = deepcopy(area)
            set_watching_area(next_area, cctv_kind[cctv_index], cctv_loc_x[cctv_index], cctv_loc_y[cctv_index], rot)
            empty_count = count_backtracking(next_area, cctv_kind, cctv_loc_x, cctv_loc_y, cctv_index + 1)
            if empty_count < smallest_count:
                smallest_count = empty_count
        return smallest_count

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    n = int(inp[0])
    m = int(inp[1])

    cctv_kind = []
    cctv_loc_x = []
    cctv_loc_y = []

    area = []
    for i in range(0, n):
        area.append([])
        inp = sys.stdin.readline().rstrip().split(" ")
        for j in range(0, m):
            now_area = int(inp[j])
            area[i].append(now_area)
            if 0 < now_area < 6 :
                cctv_kind.append(now_area)
                cctv_loc_x.append(i)
                cctv_loc_y.append(j)

    smallest_count = count_backtracking(area, cctv_kind, cctv_loc_x, cctv_loc_y, 0)
    print(smallest_count)
