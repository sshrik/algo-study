# https://www.acmicpc.net/problem/2252
import sys

fastio = sys.stdin.readline

VISIT = 1
NOT_VISIT = -1

def make_link_infor(node_num, node_link_infor):
    inner_link = [[] for _ in range(node_num)] # i 번째 index로 들어오는 것들.
    outter_link = [[] for _ in range(node_num)]# i 번째 index에서 나가는 것들.

    for node_infor in node_link_infor:
        inner_link[node_infor[1]].append(node_infor[0])
        outter_link[node_infor[0]].append(node_infor[1])
    
    return inner_link, outter_link

def find_start_link(inner_link):
    # 자신으로 들어오는게 없으면 시작 가능 node
    start_candidate = []
    for il in range(len(inner_link)):
        if len(inner_link[il]) == 0:
            start_candidate.append(il)
    return start_candidate

def all_visit(visit, node_list):
    for nl in node_list:
        if visit[nl] != VISIT:
            return False
    return True

def topology_sort(node_num, node_link_infor):
    inner_link, outter_link = make_link_infor(node_num, node_link_infor)
    
    do_seq = []
    topology_queue = find_start_link(inner_link)
    visit = [NOT_VISIT] * node_num

    while topology_queue:
        # 첫 node 꺼내서 방문하지 않은 경우에만 진행.
        now_node = topology_queue[0]
        del topology_queue[0]

        if visit[now_node] == VISIT:
            continue
        if not all_visit(visit, inner_link[now_node]):
            continue

        do_seq.append(now_node)
        visit[now_node] = VISIT

        for ol in range(len(outter_link[now_node])):
            next_node = outter_link[now_node][ol]
            if visit[next_node] == NOT_VISIT:
                topology_queue.append(next_node)
    return do_seq

def print_seq(do_seq):
    for node in do_seq:
        print(node + 1, end=" ")

if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])

    node_link_infor = []

    for _ in range(M):
        inp = fastio().rstrip().split(" ")
        node_link_infor.append( ((int(inp[0] ) - 1, int(inp[1]) - 1 )) )

    do_seq = topology_sort(N, node_link_infor)
    print_seq(do_seq)
