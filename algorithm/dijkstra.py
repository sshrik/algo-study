INFINITE = 9999999999
import heapq

def dijsktra(graph, firstIndex=0):
    '''
        graph : 2 x 2 list of linked weight. not link = False in this case.
    '''
    if firstIndex != 0:
        weight = changeNodeOrder(graph, firstIndex)
    else:
        weight = graph
    
    index = len(weight)
    d = [INFINITE for _ in range(0, index)]
    q = [-1 for _ in range(0, index)]
    d[0] = 0

    # Trace mean how to get to there.
    trace = [[0], -1, -1, -1, -1]
    stack = []

    nextIndex = getSmallestIndex(q, d)
    stack.append(nextIndex)
    
    while nextIndex != -1:
        for i in range(0, index):
            if weight[nextIndex][i] != False:
                if relax(weight, d, nextIndex, i):
                    trace[i] = stack + [i]
        nextIndex = getSmallestIndex(q, d)
        stack.append(nextIndex)
    
    return d, trace

def relax(graph, d, fromI, toJ):
    if d[fromI] + graph[fromI][toJ] < d[toJ]:
        d[toJ] = d[fromI] + graph[fromI][toJ]
        return True
    else:
        return False

def changeNodeOrder(graph, firstIndex):
    # Change firstIndex`s index item to front.
    ret = []
    tempRet = []
    tempRet += graph[firstIndex:]
    tempRet += graph[0:firstIndex]

    for retI in tempRet:
        ret.append([])
        ret[-1] += retI[firstIndex:]
        ret[-1] += retI[0:firstIndex]
    return ret

def getSmallestIndex(q, d):
    # q for visit node.
    # d for smallest values.
    ret = INFINITE
    retI = -1

    for i in range(0, len(q)):
        if q[i] == -1 and d[i] < ret:
            ret = d[i]
            retI = i
    
    if retI != -1:
        q[retI] = True
    return retI

## Index 0 to all Nodes.
d, trace = dijsktra(
    [
        [False, 6, False, 8, False], 
        [False, False, 5, 8, 1], 
        [False, 4, False, False, False], 
        [False, False, 3, False, 9], 
        [2, False, 7, False, False]
    ], 2
)

print(d)
print(trace)