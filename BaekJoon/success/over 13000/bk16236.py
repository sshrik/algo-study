# https://www.acmicpc.net/problem/16236
# 실수 1 ) 런타임에러 ( Index Error ) - 각 1 ~ 6 크기의 물고기 위치를 저장하는 List를 만들어서 사용했었는데, 그걸 지워서 성공함.

import sys
fastio = sys.stdin.readline

EMPTY = 0
SHARK = 9
NOT_VISIT = -1

dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

def can_go(fish_map, x, y, d):
    # can go d direction at (x, y)
    return 0 <= x + dir_x[d] < len(fish_map[0]) and 0 <= y + dir_y[d] < len(fish_map)

def bfs(fish_map, start_x, start_y, shark_size):
    visit = [[NOT_VISIT for _ in range(len(fish_map))] for _ in range(len(fish_map))]
    visit[start_y][start_x] = 0
    queue = [(start_x, start_y)]

    max_length = sys.maxsize

    available_list = []

    while queue:
        now = queue[0]
        del queue[0]
        now_value = visit[now[1]][now[0]]
        if now_value >= max_length:
            continue

        for d in range(4):
            if can_go(fish_map, now[0], now[1], d):
                x = now[0] + dir_x[d]
                y = now[1] + dir_y[d]
                if fish_map[y][x] != EMPTY and fish_map[y][x] < shark_size:
                    if visit[y][x] == NOT_VISIT:
                        # 다음 칸에 먹을 수 있는 물고기가 있다면 종료 조건 증가.
                        available_list.append((x, y))
                        max_length = now_value + 1
                        visit[y][x] = now_value + 1
                        queue.append((x, y))
                    
                elif fish_map[y][x] == EMPTY or fish_map[y][x] == shark_size:
                    if visit[y][x] == NOT_VISIT:
                        # 상어 몸통과 동일하거나 비어있는 경우에만 이동 가능.
                        visit[y][x] = now_value + 1
                        queue.append((x, y))

    if len(available_list) > 1:
        (return_x, return_y) = available_list[0]

        for i in range(len(available_list)):
            if return_y > available_list[i][1]:
                (return_x, return_y) = available_list[i]
            elif return_y == available_list[i][1] and return_x > available_list[i][0]:
                (return_x, return_y) = available_list[i]
        
    elif len(available_list) == 1:
        (return_x, return_y) = available_list[0]
    else:
        return_x = -1
        return_y = -1

    return return_x, return_y, visit[return_y][return_x]

def print_fish_map(fish_map):
    N = len(fish_map)
    for y in range(N):
        for x in range(N):
            print(fish_map[y][x], end="")
        print()

if __name__ == "__main__":
    N = int(fastio().rstrip())
    fish_map = []
    shark_size = 2
    time_pass = 0

    for y in range(N):
        inp = fastio().rstrip().split(" ")
        fish_map.append([])
        for x in range(N):
            fish_status = int(inp[x])
            if fish_status == SHARK:
                now_x = x
                now_y = y
            fish_map[y].append(fish_status)

    eat_fish = 0
    while True:
        # 먹을 수 있는 가장 가까운 위치의 물고기와 거기까지 가는데 걸리는 시간.
        # print("Start From", now_x, now_y)
        fish_map[now_y][now_x] = EMPTY
        now_x, now_y, spend_time = bfs(fish_map, now_x, now_y, shark_size)

        if now_x == -1:
            break

        eat_fish += 1
        if shark_size == eat_fish:
            # 사이즈만큼 물고기를 먹으면 사이즈 증가
            shark_size += 1
            eat_fish = 0
            # print("Shark Larged", shark_size)
        
        # 시간 더해주기
        time_pass += spend_time
    
        # print("End at", now_x, now_y)
        # print("Spend time", spend_time, "Total", time_pass)
        # print("Eat fish : ", fish_map[now_y][now_x])

        fish_map[now_y][now_x] = SHARK
        
        # print_fish_map(fish_map)
        # print("_____________________________")

    print(time_pass)

'''
6
0 0 2 2 0 0
0 0 3 1 0 0
0 0 3 1 0 0
0 0 0 0 0 0
0 0 0 0 0 9
0 0 0 0 0 2
'''