# https://www.acmicpc.net/problem/1012
import sys
fastio = sys.stdin.readline

EMPTY = 0
BAECHU = 1

VISIT = 1
NOT_VISIT = 0

dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

def get_count(baechu_map, M, N):
    count = 0
    visit = [[NOT_VISIT for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if visit[i][j] == NOT_VISIT and baechu_map[i][j] == BAECHU:
                bfs(baechu_map, visit, j, i)
                count += 1

    return count


def can_go(visit, x, y, d):
    M = len(visit[0])
    N = len(visit)

    return 0 <= x + dir_x[d] < M and 0 <= y + dir_y[d] < N

def bfs(baechu_map, visit, start_x, start_y):
    bfs_queue = [(start_x, start_y)]

    while bfs_queue:
        now = bfs_queue[0]
        del bfs_queue[0]

        now_x = now[0]
        now_y = now[1]
        if visit[now_y][now_x] == VISIT:
            continue
        visit[now_y][now_x] = VISIT

        for d in range(4):
            if can_go(visit, now_x, now_y, d):
                next_x = now_x + dir_x[d]
                next_y = now_y + dir_y[d]
                if baechu_map[next_y][next_x] == BAECHU:
                    bfs_queue.append((next_x, next_y))

if __name__ == "__main__":
    T = int(fastio().rstrip())
    
    for t in range(T):
        inp = fastio().rstrip().split(" ")
        M = int(inp[0])
        N = int(inp[1])
        K = int(inp[2])
        baechu_map = [[EMPTY for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            inp = fastio().rstrip().split(" ")
            x = int(inp[0])
            y = int(inp[1])
            baechu_map[y][x] = BAECHU
        print(get_count(baechu_map, M, N))
