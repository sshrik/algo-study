# https://www.acmicpc.net/problem/10026
import sys

# 동서남북 방향
dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

def can_go(N, M, x, y, direction):
    return N > x + dir_x[direction] and 0 <= x + dir_x[direction] and M > y + dir_y[direction] and 0 <= y + dir_y[direction]

def bfs(rgb_map, visited, start, N):
    bfsq = [start]
    start_color = rgb_map[start[1]][start[0]]
   #  print(start_color)

    while len(bfsq):
        now = bfsq[0]
        del bfsq[0]
        if visited[now[1]][now[0]]:
            continue
        else:
            visited[now[1]][now[0]] = True

        for d in range(4):
            x = now[0] + dir_x[d]
            y = now[1] + dir_y[d]
            if can_go(N, N, now[0], now[1], d):
                if not visited[y][x] and start_color == rgb_map[y][x]:
                    bfsq.append((x, y))
                    
def check_all_rgb(rgb_map, N):
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0

    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                # print(x, " ", y)
                bfs(rgb_map, visited, (x, y), N)
                # print_list(visited)
                count += 1

    return count

def print_list(ll):
    print("------------------------")
    for l in ll:
        for li in l:
            if li:
                print("T", end="")
            else:
                print("F", end="")

        print()

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    rgb_map = []

    # RGB[Y][X]
    for _ in range(N):
        rgb_map.append([])
        inp = sys.stdin.readline().rstrip()
        for i in range(N):
            rgb_map[-1].append(inp[i])

    non_rg = check_all_rgb(rgb_map, N)
    for i in range(N):
        for j in range(N):
            if rgb_map[i][j] == "G":
                rgb_map[i][j] = 'R'
    rg = check_all_rgb(rgb_map, N)
    print(non_rg, rg)


