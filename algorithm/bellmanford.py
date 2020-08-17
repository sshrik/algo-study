INFINITE = 9999999999

def bellmanFord(graph, firstIndex=0):
    '''
        graph : 2 x 2 list of linked weight. not link = False in this case.
    '''

    if firstIndex != 0:
        wieght = changeNodeOrder(graph, firstIndex)
    else:
        wieght = graph
    
    index = len(wieght)
    d = [INFINITE for _ in range(0, index)]
    
    # Set First d to 0.
    d[0] = 0
    roadVisit = initRoadVisit(wieght, index)
    
    for i in range(0, index):
        # For all nodes, check each edges.
        for j in range(0, index):
            for k in range(0, index):
                if roadVisit[j][k]:
                    relax(d, wieght, j, k)
    return d


def relax(d, graph, fromI, toJ):
    # Relax Function from fromI to toJ.
    if d[fromI] + graph[fromI][toJ] < d[toJ]:
        d[toJ] = d[fromI] + graph[fromI][toJ]

def initRoadVisit(graph, index):
    # Make all false list for visit or not visit check list.
    # Not linked will be expressed NOT_LINKED.
    ret = []

    for i in range(0, index):
        ret.append([])
        for j in range(0, index):
            if graph[i][j] == False:
                ret[-1].append(False)
            else:
                ret[-1].append(True)

    return ret

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

## Index 0 to all Nodes.
d = bellmanFord(
    [
        [False, 3, 8, 4, -4], 
        [False, False, False, 1, 7], 
        [False, 4, False, 5, 11], 
        [2, -1, -5, False, -2], 
        [False, False, False, 6, False]
    ], firstIndex=1
)

print(d)