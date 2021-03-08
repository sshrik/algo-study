# Kruskal Algorithm.
import sys

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

    # Step 1 : Weight 순서로 Sorting.
    from_arr, to_arr, weight_arr = sorting(from_arr, to_arr, weight_arr)
    
    # print(from_arr)
    # print(to_arr)
    # print(weight_arr)
    # Step 2 : vertex_num - 1 만큼 Edge 에서 Pick.
    now_index = 0   # Edge Index
    selected_index = [] # 이 Arr의 len이 vertex_num - 1 까지...
    parent_node = [i for i in range(0, vertex_num + 1)] # Parent 연결 정보.

    while len(selected_index) != vertex_num - 1:
        from_parent = search_top(parent_node, from_arr[now_index])
        to_parent = search_top(parent_node, to_arr[now_index])

        if from_parent != to_parent:
            # 해당 Edge를 추가해도 Cycle이 생기지 않음.
            selected_index.append(now_index)
            parent_node[from_arr[now_index]] = to_arr[now_index] # 2개의 Vertex를 연결
            parent_node[from_parent] = parent_node[to_parent]
            from_parent = to_parent # from -> now -> to 로 연결이 되었으므로, 이전의 From에서 가리키고 있던 부모는 to가 가리키고 있던 부모가 된다.
            
        setting_top(parent_node, from_arr[now_index], from_parent)  # Union Find 최적화
        setting_top(parent_node, to_arr[now_index], to_parent)  # Union Find 최적화
        now_index += 1

    # print(selected_index)
    weight_add = 0
    for si in selected_index:
        weight_add += weight_arr[si]
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