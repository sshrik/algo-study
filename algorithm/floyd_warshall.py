import sys
import heapq
INF = sys.maxsize

def floyd_warshall(graph):
    # graph : v x v 인접행렬
    # d : 인접행렬, p : 선행자 행렬, v : 정점의 갯수

    # 초기 변수 v, d, p 초기화.
    v = len(graph)
    d = copy_list(graph, v)
    p = [[] for _ in range(0, v)]

    for i in range(0, v):
        for j in range(0, v):
            p[i].append(None if d[i][j] == INF else i)
    
    for k in range(0, v):
        d = calc_next_adjacency_matrix(d, p, k, v)
    
    return d, p

def copy_list(dest, v):
    source = []

    for i in range(0, v):
        source.append([dest[i][j] for j in range(0, v)])

    return source

def calc_next_adjacency_matrix(d, p, k, v):
    next_d = [[] for _ in range(0, v)]
    
    for col in range(0, v):
        for row in range(0, v):
            relax_bool, relax_value = relax_d(d, k, col, row)
            # 만약 업데이트가 되었다면 p 값도 업데이트
            next_d[col].append(relax_value)
            p[col][row] = k if relax_bool else p[col][row]

    return next_d

def relax_d(d, k, col, row):
    # Return True if need to be updated, else return False
    # relax_bool = None if d[col][row] == d[col][k] + d[k][row] else d[col][row] > d[col][k] + d[k][row]
    relax_bool = d[col][row] > d[col][k] + d[k][row]
    relax_value = d[col][k] + d[k][row] if relax_bool else d[col][row]
    return relax_bool, relax_value

def translate_p(p, source, dest):
    col = source
    row = dest
    trace = []

    while p[col][row] != source and p[col][row] != None:
        if p[col][row] != None:
            trace.insert(0, p[col][row])
        row = p[col][row]

    trace.insert(0, source)
    trace.append(dest)
    return trace

def translate_end(p, col, row, source):
    endFlag = False

    for prev_node in p[col][row]:
        if prev_node == None or prev_node == source:
            endFlag = True
    
    return endFlag

def translate_p_list(p_list, source, dest):
    col = source
    row = dest
    trace = []

    for prev_node in p_list[col][row]:
        if prev_node == source:
            trace.append([dest])
        elif p_list[col][row][0] == None:
            trace.append([])
        else:
            trace.append(translate_p_list(p_list, source, prev_node)[0] + [dest])

    return trace
            
            

def calc_all_shortest_path(d, d_prev, p_prev):
    # graph : v x v 인접행렬
    # d : 인접행렬, p : 선행자 행렬, v : 정점의 갯수

    # 초기 변수 v, d, p 초기화.
    v = len(graph)
    p = [[] for _ in range(0, v)]

    for i in range(0, v):
        for j in range(0, v):
            p[i].append([p_prev[i][j]])

    for k in range(0, v):
        for col in range(0, v):
            for row in range(0, v):
                # 정점이 연결되어 있고, 값이 없는 경우에만 추가한다.
                if d[col][row] == d[col][k] + d[k][row]:
                    if d_prev[k][row] != INF and k not in p[col][row]:
                        p[col][row].append(k)

    return p

def print_list(lis):
    for l in lis:
        print(l)
    print()
'''
d, p = floyd_warshall([
    [INF, 2, INF, INF, INF, 2],
    [2, INF, 2, INF, INF, INF],
    [INF, 2, INF, 2, INF, INF],
    [INF, INF, 2, INF, 2, INF],
    [INF, INF, INF, 2, INF, 2],
    [2, INF, INF, INF, 2, INF],
])
'''
graph = [
    [INF, 2, INF, 6, INF, 2],
    [2, INF, 2, INF, INF, 4],
    [INF, 2, INF, 2, 4, INF],
    [6, INF, 2, INF, 2, INF],
    [INF, INF, 4, 2, INF, 2],
    [2, 4, INF, INF, 2, INF]
]
d, p = floyd_warshall(graph)

p_all = calc_all_shortest_path(d, graph, p)
print("Result below...")
print_list(d)
print_list(p)
print_list(p_all)
경로 = translate_p_list(p_all, 0, 3)

for rud in 경로:
    print("0 " + str(rud))