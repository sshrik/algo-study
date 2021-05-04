# https://www.acmicpc.net/problem/1167
import sys
fastio = sys.stdin.readline
NOT_VISIT = 0
VISIT = 1
INIT = -1

def can_go(edge, start_num, end_num):
    # Start_num -> end_num 으로 갈 수 있는 길이 있다면 해당 Load 가중치를 return.
    for e in edge[start_num]:
        if e[0] == end_num:
            return e[1]
    return -1

def get_candidate(edge, visit, now):
    # now에서 시작하는 갈 수 있는 곳 찾기.
    ret_list = []
    for e in edge[now]:
        if visit[e[0]] == NOT_VISIT:
            ret_list.append((now, e)) # e : ( $NODE_NUMBER, $EDGE_WEIGHT )
    return ret_list # ret_lsit : (start_node, (go_node, edge_weight))

def bfs(edge, N, start):
    # 가장 먼 곳 찾기.
    visit = [NOT_VISIT] * N
    visit[start] = VISIT
    weight = [0] * N

    bfs_queue = get_candidate(edge, visit, start)
    while bfs_queue:
        now = bfs_queue[0]
        del bfs_queue[0]
        before_node = now[0]
        now_node = now[1][0]
        now_weight = now[1][1]

        if visit[now_node] == VISIT:
            continue
        
        visit[now_node] = VISIT
        if weight[before_node] + now_weight > weight[now_node]:
            weight[now_node] = weight[before_node] + now_weight
        
        bfs_queue += get_candidate(edge, visit, now_node)

    max_weight = 0
    max_index = 0
    for i in range(len(weight)):
        if weight[i] > max_weight:
            max_weight = weight[i]
            max_index = i

    return max_weight, max_index

if __name__ == "__main__":
    N = int(fastio().rstrip())
    edge = [[] for _ in range(N)]

    for n in range(N):
        inp = fastio().rstrip().split(" ")
        node_num = int(inp[0]) - 1
        for i in range(1, len(inp) - 1, 2):
            edge[node_num].append( (int(inp[i]) - 1, int(inp[i + 1])) )    # Vertex 숫자 ( 0 ~ N-1 ) 과 Vertex 까지의 거리 Tuple

    weight1, index = bfs(edge, N, 0)
    weight2, _ = bfs(edge, N, index)

    print(weight2)

'''
3
1 2 4 3 5 -1
2 1 4 -1
3 1 5 -1
'''
