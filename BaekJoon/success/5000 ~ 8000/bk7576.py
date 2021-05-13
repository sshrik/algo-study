# https://www.acmicpc.net/problem/7576
import sys
from collections import deque
fastio = sys.stdin.readline

dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

def can_go(N, M, x, y, d):
    return 0 <= x + dir_x[d] < N and 0 <= y + dir_y[d] < M

def bfs(tomato_map, N, M, start_list):
    bfs_queue = deque([s for s in start_list])
    max_value = -1

    while bfs_queue:
        now = bfs_queue.popleft()

        now_x = now[0]
        now_y = now[1]

        now_value = tomato_map[now_y][now_x]

        if now_value > max_value:
            max_value = now_value

        for d in range(4):
            if can_go(N, M, now_x, now_y, d):
                next_x = now_x + dir_x[d]
                next_y = now_y + dir_y[d]
                if tomato_map[next_y][next_x] == 0:
                    bfs_queue.append((next_x, next_y))
                    tomato_map[next_y][next_x] = now_value + 1
        
    return now_value

def is_end(tomato_map, N, M):
    for y in range(M):
        for x in range(N):
            if tomato_map[y][x] == 0:
                return False
    return True

if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])
    tomato_map = [[] for _ in range(M)]
    start_list = []

    for m in range(M):
        inp = fastio().rstrip().split(" ")
        for x in range(len(inp)):
            v = int(inp[x])
            if v == 1:
                start_list.append((x, m))
            tomato_map[m].append(v)
    if len(start_list) > 0:
        max_value = bfs(tomato_map, N, M, start_list)
    # print(tomato_map)
    if is_end(tomato_map, N, M):
        print(max_value - 1)
    else:
        print(-1)