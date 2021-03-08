# Prim Algorithm.
import sys

NOT_LINKED = -1

def sorting(from_arr, to_arr, weight_arr):
    ret_from = []
    ret_to = []
    ret_weight = []
    # Weight 기준으로 정렬.
    sorting_arr = [(weight_arr[i], from_arr[i], to_arr[i]) for i in range(0, len(weight_arr))]
    sorting_arr.sort()
    for i in range(0, len(weight_arr)):
        ret_weight.append(sorting_arr[i][0])
        ret_from.append(sorting_arr[i][1])
        ret_to.append(sorting_arr[i][2])
    return ret_from, ret_to, ret_weight

def search_top(parent_node, n):
    temp_parent = n
    
    while parent_node[temp_parent] != temp_parent:
        temp_parent = parent_node[temp_parent]

    return temp_parent

def setting_top(parent_node, n, parent_number):
    # n 의 부모들을 n 의 최상단 부모로 갱신.
    temp_parent = n

    while parent_node[temp_parent] != temp_parent:
        # parent_node[temp_parent] 가 가리키는것이 본인이 아닌 경우에만 parent number를 갱신 시킴.
        next_parent = parent_node[temp_parent]
        parent_node[temp_parent] = parent_number
        temp_parent = next_parent

def get_candidate(link_data, selected_vertex):
    # selected_vertex에는 vertex number list가 들어가 있다. ( 1부터 시작함 )
    v_num = len(link_data)
    
    from_arr = []
    to_arr = []
    weight_arr = []

    for c in selected_vertex:
        for w in range(0, v_num):
            if c - 1 < w:
                if link_data[c - 1][w] != NOT_LINKED:
                    from_arr.append(c)
                    to_arr.append(w + 1)
                    weight_arr.append(link_data[c - 1][w])

    return from_arr, to_arr, weight_arr

if __name__ == "__main__":
    from_arr = []
    to_arr = []
    weight_arr = []
    inp = sys.stdin.readline().rstrip().split(" ")
    vertex_num = int(inp[0])
    edge_num = int(inp[1])

    for _ in range(0, edge_num):
        inp = sys.stdin.readline().rstrip().split(" ")
        from_arr.append(int(inp[0]))
        to_arr.append(int(inp[1]))
        weight_arr.append(int(inp[2]))

    # Step 1 : Link Data 만들기
    link_data = [[NOT_LINKED for _ in range(vertex_num)] for _ in range(vertex_num)]
    
    for e in range(0, edge_num):
        link_data[from_arr[e] - 1][to_arr[e] - 1] = weight_arr[e]
        link_data[to_arr[e] - 1][from_arr[e] - 1] = weight_arr[e]

    # Step 2 : vertex_num - 1 만큼 Edge 에서 Pick.
    selected_vertex = [1] # 이 Arr의 len이 vertex_num - 1 까지... 1부터 시작하는 MST의 Vertex Number.
    parent_node = [i for i in range(0, vertex_num + 1)] # Parent 연결 정보.
    selected_from = []
    selected_to = []
    selected_weight = []

    while len(selected_vertex) != vertex_num:
        # 만들어진 MST에서 
        cand_from, cand_to, cand_weight = get_candidate(link_data, selected_vertex)
        cand_from, cand_to, cand_weight = sorting(cand_from, cand_to, cand_weight)
        #print(cand_from)
        #print(cand_to)
        #print(cand_weight)

        for c in range(0, len(cand_from)):
            from_parent = search_top(parent_node, cand_from[c])
            to_parent = search_top(parent_node, cand_to[c])

            if from_parent != to_parent:
                # 해당 Edge를 추가해도 Cycle이 생기지 않음.
                selected_vertex.append(cand_to[c])
                selected_from.append(cand_from[c])
                selected_to.append(cand_to[c])
                selected_weight.append(cand_weight[c])
                #print("Select ", cand_from[c], " to ", cand_to[c], " : ", cand_weight[c])

                parent_node[cand_from[c]] = cand_to[c] # 2개의 Vertex를 연결
                parent_node[from_parent] = parent_node[to_parent]
                from_parent = to_parent # from -> now -> to 로 연결이 되었으므로, 이전의 From에서 가리키고 있던 부모는 to가 가리키고 있던 부모가 된다.
                setting_top(parent_node, cand_from[c], from_parent)  # Union Find 최적화
                setting_top(parent_node, cand_to[c], to_parent)  # Union Find 최적화
                break
            
            setting_top(parent_node, cand_from[c], from_parent)  # Union Find 최적화
            setting_top(parent_node, cand_to[c], to_parent)  # Union Find 최적화
        
        #print(selected_vertex)

    # print(selected_index)
    weight_add = 0
    for si in selected_weight:
        weight_add += si
    print(weight_add)


'''
3 3
1 2 1
2 3 2
1 3 3

7 9
1 2 2
1 3 4
2 3 5
2 4 3
3 4 6
3 5 2
3 6 7
5 6 17
5 7 30
'''