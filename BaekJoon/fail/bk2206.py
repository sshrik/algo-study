# https://www.acmicpc.net/problem/2206
import sys
fastio = sys.stdin.readline
dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

WALL = 1
EMPTY = 0
NOT_VISITED = 0
VISITED = 1

def can_go(meero_map, x, y, d):
    return 0 <= x + dir_x[d] < len(meero_map[0]) and 0 <= y + dir_y[d] < len(meero_map)

def search_meero(meero_map):
    # (0, 0) 에서 시작하는 미로 최단거리를 찾는다.
    meero_copy = [[meero_map[h][w] for w in range(len(meero_map[h]))] for h in range(len(meero_map))]
    visit_map = [[NOT_VISITED for _ in range(len(meero_map[0]))] for _ in range(len(meero_map))]
    meero_queue = [(0, 0)]
    meero_copy[0][0] = 2

    while meero_queue:
        now = meero_queue[0]
        del meero_queue[0]
        
        if visit_map[now[1]][now[0]] != NOT_VISITED:
            continue

        visit_map[now[1]][now[0]] = VISITED
        now_number = meero_copy[now[1]][now[0]]
        
        for d in range(4):
            if can_go(meero_map, now[0], now[1], d):
                x = dir_x[d] + now[0]
                y = dir_y[d] + now[1]
                if meero_map[y][x] == EMPTY and visit_map[y][x] == NOT_VISITED:
                    meero_copy[y][x] = now_number + 1
                    
                    if x == len(meero_map[0]) - 1 and y == len(meero_map) - 1:
                        return meero_copy[y][x] - 1

                    meero_queue.append((x, y))

    return sys.maxsize

def check_wall_condition(meero_map, x, y):
    wall_number = 0
    for d in range(4): 
        if can_go(meero_map, x, y, d):
            if meero_map[y + dir_y[d]][x + dir_x[d]] == WALL:
                wall_number += 1

    return wall_number <= 2

if __name__ == "__main__":
    inp = fastio().split(" ")
    N = int(inp[0])
    M = int(inp[1])

    meero_map = [[] for _ in range(N)]

    wall_list = []
    for n in range(N):
        inp = fastio()
        for m in range(M):
            now = int(inp[m])
            if now == 1:
                wall_list.append((m, n))
            meero_map[n].append(now)
    
    small = search_meero(meero_map)
    
    for wl in wall_list:
        if check_wall_condition(meero_map, wl[0], wl[1]):
            meero_map[wl[1]][wl[0]] = EMPTY
            dist = search_meero(meero_map)
            meero_map[wl[1]][wl[0]] = WALL
            small = small if dist > small else dist
    
    if small == sys.maxsize:
        print(-1)
    else:
        print(small)

'''
6 4
0000
1110
1000
0000
0111
0000
'''
    