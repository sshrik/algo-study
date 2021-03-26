import sys
import heapq
INF = sys.maxsize

def dijkstra(weight_list, V, start):
    d = [INF for _ in range(0, V)]
    weight_heap = []
    # Heap에 (weight, index) 를 순서로 넣어준다.
    heapq.heappush(weight_heap, (0, start)) # 첫번째 시작하는 곳의 d는 0으로 만들어 줘야 함.

    while len(weight_heap) > 0:
        # Setting now value.
        now = heapq.heappop(weight_heap)
        now_weight = now[0]
        now_indx = now[1]
    
        if d[now_indx] < now_weight:
            continue
        
        d[now_indx] = now_weight
        for i in range(0, V):
            try:
                if weight_list[now_indx][i] + d[now_indx] < d[i]:
                    # 만약 relax 결과가 더 낮다면, d[i] 값을 갱신 해 준다.
                    d[i] = weight_list[now_indx][i] + d[now_indx]
                    heapq.heappush(weight_heap, (d[i], i))
            except:
                pass
    return d


def get_next_index(d, visited, V):
    next_heap = [(INF, -1)]

    for v in range(0, V):
        if not visited[v]:
            heapq.heappush(next_heap, (d[v], v))
    
    return next_heap[0][1]

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")
    V = int(inp[0])
    E = int(inp[1])
    start_idx = int(sys.stdin.readline().rstrip()) - 1

    weight_list = [ {} for _ in range(0, V)]

    for _ in range(0, E):
        inp = sys.stdin.readline().rstrip().split(" ")
        start_v = int(inp[0]) - 1
        end_v = int(inp[1]) - 1
        weight = int(inp[2])
        
        # 노드간 간선이 2개 이상이면 더 짧은것만 표기.
        try:
            if weight_list[start_v][end_v] > weight:
                weight_list[start_v][end_v] = weight
        except:
            weight_list[start_v][end_v] = weight
        
    value = dijkstra(weight_list, V, start_idx)
    for i in range(0, V):
        if value[i] != INF:
            print(value[i])
        else:
            print("INF")
    