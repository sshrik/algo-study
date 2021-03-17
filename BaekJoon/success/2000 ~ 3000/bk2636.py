# https://www.acmicpc.net/problem/2636
import sys

dir_x = [0, 0, 1, -1]
dir_y = [1, -1, 0, 0]
NOT_VISITED = 2
VISITED = 3
CHEESE = 1
EMPTY = 0
OUTER = -1

def get_dfs_map(cheese_map):
    # 0, 0 에서 시작하는 DFS로 OUTER, CHEESE, EMPTY 를 골라낸 것을 return.
    dfs_queue = [(0, 0)]
    outer_map = [[cheese_map[h][w] for w in range(len(cheese_map[h]))] for h in range(len(cheese_map))]
    visited_map = [[NOT_VISITED for _ in range(len(cheese_map[0]))] for _ in range(len(cheese_map))]

    while dfs_queue:
        now = dfs_queue[0]
        del dfs_queue[0]

        x = now[0]
        y = now[1]
        if visited_map[y][x] != NOT_VISITED:
            # 방문했다면 PASS
            continue
        visited_map[y][x] = VISITED

        if outer_map[y][x] == EMPTY or outer_map[y][x] == OUTER:
            outer_map[y][x] = OUTER
            for d in range(4):
                if can_go(outer_map, x, y, d):
                    if outer_map[y + dir_y[d]][x + dir_x[d]] == EMPTY:
                        dfs_queue.append((x + dir_x[d], y + dir_y[d]))
                    elif outer_map[y + dir_y[d]][x + dir_x[d]] == OUTER and visited_map[y + dir_y[d]][x + dir_x[d]] == NOT_VISITED:
                        dfs_queue.append((x + dir_x[d], y + dir_y[d]))

    return outer_map

def print_map(cheese_map):
    for h in range(len(cheese_map)):
        for w in range(len(cheese_map[h])):
            if cheese_map[h][w] == OUTER:
                print("_", end="")
            elif cheese_map[h][w] == CHEESE:
                print("#", end="")
            else:
                print(" ", end="")
        print()

def get_next_chees_map(cheese_map):
    result_arr = []
    for y in range(len(cheese_map)):
        for x in range(len(cheese_map[0])):
            if will_dissapper(cheese_map, x, y):
                result_arr.append((x, y))
    return result_arr

def will_dissapper(cheese_map, x, y):
    for d in range(4):
        if can_go(cheese_map, x, y, d) and cheese_map[y + dir_y[d]][x + dir_x[d]] == OUTER:
            return True
    return False
    
def can_go(cheese_map, x, y, direction):
    return 0 <= x + dir_x[direction] < len(cheese_map[0]) and 0 <= y + dir_y[direction] < len(cheese_map)

def check_all_clear(cheese_map):
    for y in range(len(cheese_map)):
        for x in range(len(cheese_map[0])):
            if cheese_map[y][x] == CHEESE:
                return False
    return True


if __name__ == "__main__":
    inp = sys.stdin.readline().split(" ")
    height = int(inp[0])
    width = int(inp[1])

    cheese_map = [[] for _ in range(height)]
    for h in range(height):
        inp = sys.stdin.readline().split(" ")
        for i in inp:
            cheese_map[h].append(int(i))
    
    count = 0
    last_cheese_map = []
    while not check_all_clear(cheese_map):
        cheese_map = get_dfs_map(cheese_map)
        count += 1
        
        # print_map(cheese_map)

        wd_list = get_next_chees_map(cheese_map)
        last_cheese_map = [[cheese_map[h][w] for w in range(len(cheese_map[h]))] for h in range(len(cheese_map))]
        for wd in wd_list:
            cheese_map[wd[1]][wd[0]] = OUTER
        
    print(count)

    count = 0
    for h in range(len(last_cheese_map)):
        for w in range(len(last_cheese_map[h])):
            if last_cheese_map[h][w] == CHEESE:
                count += 1

    print(count)

'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''