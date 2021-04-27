# https://www.acmicpc.net/problem/1260
import sys

fastio = sys.stdin.readline


def get_candidate(link_data, visit, now_node):
    length = len(visit)
    candidate = []

    for next_node in range(0, length):
        if ( not visit[next_node] ) and link_data[now_node][next_node]:
            candidate.append(next_node)

    return candidate

def dfs(link_data, start_node):
    ret_list = []
    visit = [False for _ in range(len(link_data))]
    dfs_stack = [(start_node, -1, get_candidate(link_data, visit, start_node))]

    while dfs_stack:
        now = dfs_stack[-1]
        now_node = now[0]
        now_index = now[1]
        now_cand = now[2]

        del dfs_stack[-1]

        if now_index == -1:
            if visit[now_node]:
                continue
            visit[now_node] = True
            ret_list.append(now_node)

        if now_index == len(now_cand) - 1:
            continue

        now_index += 1
        dfs_stack.append((now_node, now_index, now_cand))

        next_node = now_cand[now_index]
        dfs_stack.append((next_node, -1, get_candidate(link_data, visit, next_node)))

    return ret_list

def bfs(link_data, start_node):
    ret_list = []
    visit = [False for _ in range(len(link_data))]
    bfs_queue = [start_node]

    while bfs_queue:
        now_node = bfs_queue[0]
        del bfs_queue[0]

        if visit[now_node]:
            continue

        visit[now_node] = True
        ret_list.append(now_node)

        bfs_queue = bfs_queue + get_candidate(link_data, visit, now_node)
    
    return ret_list

def print_trace(trace):
    for tr in trace:
        print(tr + 1, end=" ")
    print()

if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])
    V = int(inp[2])

    link_data = [[False for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        inp = fastio().rstrip().split(" ")
        i = int(inp[0]) - 1
        j = int(inp[1]) - 1
        link_data[i][j] = True
        link_data[j][i] = True

    print_trace(dfs(link_data, V - 1))
    print_trace(bfs(link_data, V - 1))
