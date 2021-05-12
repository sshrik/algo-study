# https://www.acmicpc.net/problem/1238
import sys
import heapq
fastio = sys.stdin.readline

NOT_LINK = -1
INIT_VALUE = sys.maxsize

def get_candidate(linkData, start, N):
    # Start 에서 갈 수 있는 dest의 목록.
    return linkData[start]

def get_shortest_path(linkInfor, linkData, N, start, dest=-1):
    # start 에서 dest까지 갈 때 최단거리 List를 return
    visit = [False] * N
    distance = [INIT_VALUE] * N
    distance[start] = 0
    nextHeap = [(0, start)] # (start ~ number 까지 최단거리 weight, 마을 number)

    while nextHeap:
        now = heapq.heappop(nextHeap)
        _, now_node = now

        if visit[now_node]:
            continue
        visit[now_node] = True

        if now_node == dest:
            break

        nextCandidate = get_candidate(linkData, now_node, N)

        for nc in nextCandidate:
            if distance[nc] > distance[now_node] + linkInfor[now_node][nc]:
                distance[nc] = distance[now_node] + linkInfor[now_node][nc]
                heapq.heappush(nextHeap, (distance[nc], nc))
    
    return distance

if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])
    X = int(inp[2]) - 1

    linkInfor = [[NOT_LINK for _ in range(N)] for _ in range(N)]
    linkData = [[] for _ in range(N)]

    for _ in range(M):
        inp = fastio().rstrip().split(" ")
        start_node = int(inp[0]) - 1
        end_node = int(inp[1]) - 1
        take_time = int(inp[2])
        if linkInfor[start_node][end_node] == NOT_LINK:
            linkInfor[start_node][end_node] = take_time
            linkData[start_node].append(end_node)
        elif linkInfor[start_node][end_node] > take_time:
            linkInfor[start_node][end_node] = take_time

    distance = [0 for _ in range(N)]
    for i in range(N):
        # print(get_shortest_path(linkInfor, N, i, X))
        distance[i] += get_shortest_path(linkInfor, linkData, N, i, X)[X]
    
    xToN = get_shortest_path(linkInfor, linkData, N, X)
    # print(xToN)

    for i in range(N):
        distance[i] += xToN[i]

    print(max(distance))

