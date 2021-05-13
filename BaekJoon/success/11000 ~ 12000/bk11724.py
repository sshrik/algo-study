# https://www.acmicpc.net/problem/11724
import sys
from collections import deque
fastio = sys.stdin.readline

def get_cand(link_infor, visit, now, N):
    res = []

    for n in range(N):
        if link_infor[now][n] and not visit[n]:
            res.append(n)

    return res

def bfs(link_infor, visit, start, N):
    bfs_queue = deque([start])

    while bfs_queue:
        now = bfs_queue.popleft()

        if visit[now]:
            continue
        visit[now] = True
        bfs_queue += get_cand(link_infor, visit, now, N)

if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])

    visited = [False for _ in range(N)]
    link_infor = [[False for _ in range(N)]for _ in range(N)]

    for _ in range(M):
        inp = fastio().rstrip().split(" ")
        start = int(inp[0]) - 1
        end = int(inp[1]) - 1

        link_infor[end][start] = True
        link_infor[start][end] = True

    count = 0
    for n in range(N):
        if not visited[n]:
            bfs(link_infor, visited, n, N)
            count += 1
    
    print(count)

