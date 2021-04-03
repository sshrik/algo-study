# https://www.acmicpc.net/problem/1520
import sys

dir_x = [0, 0, 1, -1]
dir_y = [1, -1, 0, 0]

def can_go(down_map, x, y, direction):
    now_value = down_map[x][y]
    max_x = len(down_map)
    max_y = len(down_map[0])

    next_x = x + dir_x[direction]
    next_y = y + dir_y[direction]
    if 0 <= next_x < max_x and 0 <= next_y < max_y:
        if now_value > down_map[next_x][next_y]:
            return True
    
    return False

def get_next_step(down_map, x, y):
    # 4방향 탐색 후 갈 수 있는 위치의 (x, y)쌍 List로 Return.
    ret_list = []
    for d in range(0, 4):
        if can_go(down_map, x, y, d):
            ret_list.append((x + dir_x[d], y + dir_y[d]))
    return ret_list

def set_visited(moving_stack, visit_map):
    for i in range(len(moving_stack)):
        now_candidate = moving_stack[i][0]
        step_index = moving_stack[i][1]

        visit_map[now_candidate[step_index][0]][now_candidate[step_index][1]] += 1

def get_back(moving_stack):
    while moving_stack:
        now_step = moving_stack[-1]
        del moving_stack[-1]
        now_candidate = now_step[0]
        step_index = now_step[1]

        # 아직 갈게 있는 갈림길까지 back.
        if len(now_candidate) >= step_index + 1:
            break

def check_visited(next_step):
    for ns in next_step:
        if visit_map[ns[0]][ns[1]] == VISITED:
            return True
    return False

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    n = int(inp[0])
    m = int(inp[1])

    visit_map = [[0 for _ in range(m)] for _ in range(n)]
    down_map = [[] for _ in range(n)]
    for i in range(0, n):
        inp = sys.stdin.readline().rstrip().split(" ")
        for inpp in inp:
            down_map[i].append(int(inpp))

    moving_stack = []
    count = 0
    next_step = get_next_step(down_map, 0, 0)   # (0, 0) 에서 출발하는 가능한 다음 단계를 구함.
    moving_stack.append((next_step, -1))

    while moving_stack:
        now_step = moving_stack[-1]
        del moving_stack[-1]
        now_candidate = now_step[0]
        step_index = now_step[1]

        # 더 갈곳이 없다면 continue.
        if len(now_candidate) == step_index + 1:
            continue

        step_index += 1
        now_x = now_candidate[step_index][0]
        now_y = now_candidate[step_index][1]
        
        # 더 갈곳이 있을 수 있으니 다시 push.
        moving_stack.append((now_candidate, step_index))
        
        next_step = get_next_step(down_map, now_x, now_y)
        real_next_step = []
        for ns in next_step:
            if visit_map[ns[0]][ns[1]] > 0:
                set_visited(moving_stack, visit_map)
            elif ns[0] == n-1 and ns[1] == m-1):
                count += 1
            else:
                real_next_step.append(ns)
        if len(real_next_step) == 0:
            print(moving_stack)
            print(next_step)
            print(count)
            get_back(moving_stack)
        else:
            moving_stack.append((real_next_step, -1))

    print(count)
    