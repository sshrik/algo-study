# https://www.acmicpc.net/problem/2178
import sys

# 동서남북 방향
dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

INIT_VALUE = sys.maxsize - 20

# 여기에서 y + dir_y 로 조건을 줘야하는데 실수했었음.
def can_go(M, N, x, y, direction):
    return M > x + dir_x[direction] and 0 <= x + dir_x[direction] and N > y + dir_y[direction] and 0 <= y + dir_y[direction]

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])
    miro = []
    count_map = []

    for _ in range(N):
        miro.append([])
        count_map.append([])
        inp = sys.stdin.readline().rstrip()
        for i in inp:
            miro[-1].append(int(i))
            count_map[-1].append(INIT_VALUE)
    
    bfsq = [(0, 0)]
    count = 1
    count_map[0][0] = count # Visited 역할도 같이 함.

    while len(bfsq):
        now = bfsq[0]
        count = count_map[now[1]][now[0]] + 1
        del bfsq[0]

        # 여기에서 x, y 를 거꾸로 써서 에러가 났었음..
        for d in range(4):
            x = now[0] + dir_x[d]
            y = now[1] + dir_y[d]
            if can_go(M, N, now[0], now[1], d) and miro[y][x] != 0:
                if count_map[y][x] > count:
                    count_map[y][x] = count
                    bfsq.append((x, y))

    print(count_map[N - 1][M - 1])

