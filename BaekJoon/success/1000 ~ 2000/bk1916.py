#https://www.acmicpc.net/problem/1916
# 실수 1 : 이미 방문한 node는 빼고 탐색해야하는 것에서 틀렸었다.
# 실수 2 : 간선이 여러개 올 수 있어서 틀렸었다.

import sys
INF = sys.maxsize

def get_next(visited, distance):
    smallest_index = -1

    for n in range(len(visited)):
        if not visited[n]:
            if smallest_index == -1:
                smallest_index = n
            elif distance[n] < distance[smallest_index]:
                smallest_index = n

    return smallest_index

def check_all_visited(visited):
    for v in visited:
        if not v:
            return False
    return True

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    dist_map = [[INF for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        inp = sys.stdin.readline().rstrip().split(" ")
        if int(inp[2]) < dist_map[int(inp[0]) - 1][int(inp[1]) - 1]:
            dist_map[int(inp[0]) - 1][int(inp[1]) - 1] = int(inp[2])
    
    visited = [False for _ in range(N)]
    distance = [INF for _ in range(N)]

    inp = sys.stdin.readline().rstrip().split(" ")
    start = int(inp[0]) - 1
    end = int(inp[1]) - 1
    
    for n in range(N):
        distance[n] = dist_map[start][n]    # node start에서 n 까지의 바로 가는 거리.
    visited[start] = True

    while not check_all_visited(visited):
        now_index = get_next(visited, distance)
        visited[now_index] = True

        for n in range(N):
            if not visited[n]:
                if distance[n] > distance[now_index] + dist_map[now_index][n]:
                    distance[n] = distance[now_index] + dist_map[now_index][n]
        #print(distance)
    print(distance[end])
'''
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

6
9
1 2 1
1 3 1
2 3 1
3 4 2
4 5 1
1 5 4
1 6 7
5 6 1
4 6 1
1 6

6
8
1 2 1
2 1 1
2 3 1
3 4 1
4 5 1
5 6 1
1 6 0
6 5 1
2 5

'''