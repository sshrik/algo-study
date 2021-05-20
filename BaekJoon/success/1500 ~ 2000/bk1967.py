# https://www.acmicpc.net/problem/1967
import sys
from collections import deque
fastio = sys.stdin.readline

NOT_LINK = -1

def get_candidate(link_info, visit, N, now):
    result = []
    for n in link_info[now]:
        if not visit[n]:
            result.append(n)
    return result

def search_longest_path(link_info, N, start_at):
    bfs_queue = deque([(0, start_at)])
    visit = [False] * N
    max_path = 0
    max_dest = 0

    while bfs_queue:
        now = bfs_queue.popleft()
        now_value = now[0]
        now_start = now[1]

        if visit[now_start]:
            continue
        visit[now_start] = True
        if max_path < now_value:
            max_path = now_value
            max_dest = now_start

        result = get_candidate(link_info, visit, N, now_start)

        for r in result:
            bfs_queue.append((link_info[now_start][r] + now_value, r))
    return max_path, max_dest


if __name__ == "__main__":
    N = int(fastio().rstrip())
    
    link_count = [0] * N
    link_info = [{} for _ in range(N)]

    for _ in range(N - 1):
        inp = fastio().rstrip().split(" ")
        n1 = int(inp[0]) - 1
        n2 = int(inp[1]) - 1
        weight = int(inp[2])
        link_info[n1][n2] = weight
        link_info[n2][n1] = weight
        link_count[n1] += 1
        link_count[n2] += 1

    max_path, max_dest = search_longest_path(link_info, N, 0)
    max_path, _ = search_longest_path(link_info, N, max_dest)

    print(max_path)
