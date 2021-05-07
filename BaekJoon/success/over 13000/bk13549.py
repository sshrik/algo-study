# https://www.acmicpc.net/problem/13549
import sys
fastio = sys.stdin.readline
POINT_MAX = 200000

def get_next(now):
    return [now - 1 >= 0, now + 1 < POINT_MAX, now * 2 < POINT_MAX]

def bfs(N, K):
    if N == K:
        return 0
    visit = [False] * POINT_MAX
    bfs_queue = [(0, N)] # (걸린 시간, 현재 위치)

    while bfs_queue:
        now = bfs_queue[0]
        del bfs_queue[0]
        now_sec = now[0]
        now_loc = now[1]

        if visit[now_loc]:
            continue
        visit[now_loc] = True

        next_avail = get_next(now_loc)

        if next_avail[2]:
            if now_loc * 2 == K:
                return now_sec
            if not visit[now_loc * 2]:
                bfs_queue.append((now_sec, now_loc * 2))
        if next_avail[0]:
            if now_loc - 1 == K:
                return now_sec + 1
            if not visit[now_loc - 1]:
                bfs_queue.append((now_sec + 1, now_loc - 1))
        if next_avail[1]:
            if now_loc + 1 == K:
                return now_sec + 1
            if not visit[now_loc + 1]:
                bfs_queue.append((now_sec + 1, now_loc + 1))

if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    K = int(inp[1])

    print(bfs(N, K))

