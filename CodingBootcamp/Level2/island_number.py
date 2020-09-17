# [1, 1, 1, 1, 0]
# [1, 1, 0, 1, 0]
# [1, 1, 0, 0, 0]
# [0, 0, 0, 0, 0]
# 1은 땅, 0이 바다인 경우, 섬의 갯수를 찾아라.


import sys

LAND = 1
OCEAN = 0

# 동 서 남 북으로 이동시 x, y, 의 변화
x_diff = [0, 0, 1, -1]
y_diff = [1, -1, 0, 0]

def dfs(inp_map, visited, n, m, x, y):
    # Depth first seach for starting (x, y).
    next_queue = [(x, y)]

    while len(next_queue) != 0:
        # Check now check coordinate.
        (now_x, now_y) = next_queue[0]
        del next_queue[0]
        # 이미 방문한 곳이면 가지 않는다.
        if visited[now_x][now_y]:
            continue

        visited[now_x][now_y] = True

        # 모든 방향에 대해서, 갈 수 있는 경우를 검색.
        for direction in range(0, 4):
            if can_go(n, m, now_x, now_y, direction):
                # 방문하지 않았던 땅 일 경우에만 Queue 에 추가한다.
                if inp_map[now_x + x_diff[direction]][now_y + y_diff[direction]] == LAND and not visited[now_x + x_diff[direction]][now_y + y_diff[direction]]:
                    next_queue.append((now_x + x_diff[direction], now_y + y_diff[direction]))

def can_go(n, m, x, y, direction):
    return x + x_diff[direction] < n and x + x_diff[direction] > -1 and y + y_diff[direction] < m and y + y_diff[direction] > -1


if __name__ == "__main__":
    inp = sys.stdin.readline().strip().split(" ")
    n = int(inp[0])
    m = int(inp[1])

    inp_map = []
    visited = []

    for _ in range(0, n):
        inp_map.append([])
        visited.append([])
        inp = sys.stdin.readline().strip().split(" ")
        for i in range(0, m):
            inp_map[-1].append(int(inp[i]))
            visited[-1].append(False)

    continent = 0

    for x in range(0, n):
        for y in range(0, m):
            if inp_map[x][y] == LAND and not visited[x][y]: 
                dfs(inp_map, visited, n, m, x, y)
                continent += 1


    print(continent)
