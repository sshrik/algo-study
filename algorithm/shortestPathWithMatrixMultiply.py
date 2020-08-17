import sys
import heapq

INF = sys.maxsize

def shortestPathWithMatrixMultiply(graph):
    # graph : 2 x 2 matrix with from me to me = 0, not linked = INF
    v = len(graph) # V는 정점의 갯수.

    l = graph
    for _ in range(0, v):
        l = spMtrixMultipy(l, graph, v)
    
    return l

def shortestPathWithMatrixMultiplyWithPower(graph):
    # graph : 2 x 2 matrix with from me to me = 0, not linked = INF
    v = len(graph) # V는 정점의 갯수.

    l = graph
    m = 1
    while m < v - 1:
        l = spMtrixMultipy(l, l, v)
        m = 2 * m

    return l


def spMtrixMultipy(graph1, graph2, v):
    # ret = return value
    ret = [[None for _ in range(0, v)] for _ in range(0, v)]
    
    for i in range(0, v):
        for j in range(0, v):
            minVal = graph1[i][0] + graph2[0][j]
            for k in range(0, v):
                if minVal > graph1[i][k] + graph2[k][j]:
                    minVal = graph1[i][k] + graph2[k][j]
            ret[i][j] = minVal
    
    return ret

print(shortestPathWithMatrixMultiplyWithPower([
    [0, 2, INF, INF, 2],
    [2, 0, 2, INF, 2],
    [INF, 2, 0, 2, INF],
    [INF, INF, 2, 0, 2],
    [2, INF, INF, 2, 0],
]))