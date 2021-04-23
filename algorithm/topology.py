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

        do_seq.append(now_node)
        visit[now_node] = VISIT

        for ol in range(len(outter_link[now_node])):
            next_node = outter_link[now_node][ol]
            if visit[next_node] == NOT_VISIT:
                topology_queue.append(next_node)
    return do_seq

def print_seq(do_seq):
    for node in do_seq[:-1]:
        print(node, "->", end=" ")
    print(do_seq[-1])

if __name__ == "__main__":
    node_num = 9
    node_link_infor = [(0, 3), (1, 3), (1, 4), (2, 5), (2, 4), (3, 6), (5, 6), (4, 7), (6, 8), (7, 8)]
    do_seq = topology_sort(node_num, node_link_infor)
    print(do_seq)
    print_seq(do_seq)

