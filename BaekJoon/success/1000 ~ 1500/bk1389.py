# https://www.acmicpc.net/problem/1389
import sys
INF = sys.maxsize
fastio = sys.stdin.readline

def search_all_pair(friend_link, N):
    # 플로이드 워셔 알고리즘으로 모든 Pair 최단거리 탐색
    d = make_link_length_graph(friend_link, N)
    
    for mid in range(N):
        d = next_step(d, mid, N)    
    return d

def make_link_length_graph(friend_link, N):
    link_length = [[INF for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if friend_link[i][j]:
                link_length[i][j] = 1
                link_length[j][i] = 1

    return link_length


def relax_function(d, start, end, mid):
    # start 에서 시작해서 mid 를 거쳐서 end 로 갈 때의 거리가 그냥과 비교했을 때?
    relax_bool = d[start][end] > d[start][mid] + d[mid][end]
    relax_value = d[start][mid] + d[mid][end] if relax_bool else d[start][end]
    return relax_value

def next_step(d, mid, N):
    next_d = [[] for _ in range(N)]
    for start in range(N):
        for end in range(N):
            relax_value = relax_function(d, start, end, mid)
            next_d[start].append(relax_value)
    return next_d


if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])

    friend_link = [[False for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        inp = fastio().rstrip().split(" ")
        f1 = int(inp[0]) - 1
        f2 = int(inp[1]) - 1
        friend_link[f1][f2] = True
        friend_link[f2][f1] = True

    short_pair = search_all_pair(friend_link, N)
    smallest = INF
    smallest_indx = INF
    for i in range(N):
        kb_num = sum(short_pair[i]) - short_pair[i][i]
        if kb_num < smallest:
            smallest = kb_num
            smallest_indx = i

    print(smallest_indx + 1)
