import heapq
import sys

INF = sys.maxsize

# Calc node 0 to else shortest path.
def dijkstraWIthHeap(graph, start):
    heap = []
    # d( distance weight ) 을 모두 무한대로 두고 시작. 첫번쨰 d는 0으로 초기화함.
    d = [INF for _ in range(0, len(graph))]
    d[start] = 0
    # stack 은 지나왔던 노드 trace는 0에서 출발해서 index node 까지 가기 위해 지나왔던 노드들.
    stack = [start] # start으로 시작하니깐..
    trace = [[] for _ in range(0, len(graph))]
    # 첫 노드를 0 으로 삽입. (가중치, 순서, 지나온 길)
    heapq.heappush(heap, (0, start, stack))

    # heap의 변수가 모두 떨어질 떄 까지
    while heap:
        weight, now, stack = heapq.heappop(heap)

        # heap에 들어있던 가중치가 현재 가장 짧은 거리보다 더 큰 경우는 무시한다.
        # 여기가 좀 아리송했던 부분인데, 다른 노드를 통해서 계산하던 도중 값이 더 작아진 경우는 mutable한 heap 내부 값을 어떻게 변경해야 하나 했는데
        # 변경하지 않고, 다시 추가한 다음 진행하는 것으로 해결 했었음. ( 다른 사람의 코드 )
        if d[now] < weight:
            continue
        
        for nextIndex in range(0, len(graph[now])):
            addWeight = graph[now][nextIndex]
            if addWeight != INF:
                # 만약 길이 있고, 그 길로 갔을 때 최단거리가 된다면 최단거리를 업데이트.
                if d[now] + addWeight < d[nextIndex]:
                    # 최단거리가 업데이트 되었으므로, 이동한 stack에 추가하고, trace도 업데이트.
                    trace[nextIndex] = [stack[:] + [nextIndex]]

                    # ( 가중치, 순서, 지나온 길 + 갈 길 ) tuple을 heap에 추가함.
                    d[nextIndex] = d[now] + addWeight
                    heapq.heappush(heap, (d[nextIndex], nextIndex, stack + [nextIndex]))
                elif d[now] + addWeight == d[nextIndex]:
                    # 최단거리가 동일한 경우에도 trace 업데이트 - 길이 여러개인 경우
                    trace[nextIndex].append(stack[:] + [nextIndex])

    return d, trace

inp = [
    [0, 1, 1],
    [0, 2, 2],
    [0, 3, 3],
    [0, 4, 4],
    [1, 4, 5],
    [1, 5, 6],
    [2, 4, 7],
    [3, 6, 8],
    [4, 0, 9],
    [4, 5, 10],
    [6, 5, 11]
]
V = 7

dkInp = [[False for _ in range(0, V)] for _ in range(0, V)]

for ip in inp:
    dkInp[ip[0]][ip[1]] = ip[2]

dkInp = [
    [INF, 2, INF, 6, INF, 2],
    [2, INF, 2, INF, INF, 4],
    [INF, 2, INF, 2, 4, INF],
    [6, INF, 2, INF, 2, INF],
    [INF, INF, 4, 2, INF, 2],
    [2, 4, INF, INF, 2, INF]
]
d, trace = dijkstraWIthHeap(dkInp, 1)

print(d)
print(trace)