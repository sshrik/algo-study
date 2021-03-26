# https://www.acmicpc.net/problem/2589
import sys
fastio = sys.stdin.readline

VISITED = 1
NOT_VISITED = 0
LAND = "L"
WATER = "W"

dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

def can_go(treasure_map, x, y, d):
    return 0 <= x + dir_x[d] < len(treasure_map[0]) and 0 <= y + dir_y[d] < len(treasure_map)

def bfs(treasure_map, start_x, start_y):
    height = len(treasure_map)
    width = len(treasure_map[0])
    visit = [[NOT_VISITED for _ in range(width)] for _ in range(height)]
    length_map = [[0 for _ in range(width)] for _ in range(height)]

    next_queue = [(start_x, start_y)]
    highest_value = 0

    while next_queue:
        now = next_queue[0]
        del next_queue[0]
        x = now[0]
        y = now[1]

        if visit[y][x] == VISITED:
            continue
        
        now_value = length_map[y][x]
        if highest_value < now_value:
            highest_value = now_value

        visit[y][x] = VISITED

        for d in range(4):
            if can_go(treasure_map, x, y, d):
                next_x = x + dir_x[d]
                next_y = y + dir_y[d]
                if treasure_map[next_y][next_x] == LAND:
                    length_map[next_y][next_x] = now_value + 1
                    next_queue.append((next_x, next_y))
        
    return highest_value

if __name__ == "__main__":
    inp = fastio().split(" ")
    height = int(inp[0])
    width = int(inp[1])
    treasure_map = []

    for _ in range(height):
        treasure_map.append(fastio())
    
    answer = 0

    for h in range(height):
        for w in range(width):
            if treasure_map[h][w] == LAND:
                bfs_return = bfs(treasure_map, w, h)
                answer = bfs_return if bfs_return > answer else answer
    
    print(answer)