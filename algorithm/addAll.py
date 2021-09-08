import math

def add_up_dp(given_list, N):
    add_up_list = [given_list[0]]
    for i in range(1, N):
        add_up_list.append(add_up_list[i - 1] + given_list[i])
    return add_up_list

def get_add_total(add_up_list, start, end):
    # given_list[end] 부터 given_list[start + 1] 까지의 합
    return add_up_list[end] - add_up_list[start]

def make_seg_tree(given_list, N):
    MAX_SIZE = 1
    while MAX_SIZE < N:
        MAX_SIZE *= 2

    seg_tree = [0 for _ in range(MAX_SIZE * 2 - 1)]
    init_tree(seg_tree, given_list, 0, 0, N - 1)
    return seg_tree

def init_tree(seg_tree, given_list, index, start, end):
    # seg_tree[index] 의 값을 계산한다. 그 값은 start ~ end 까지의 합이다. 
    # 그리고 그런 값을 return 한다.
    if start == end:
        seg_tree[index] = given_list[start]
    else:
        mid = int((start + end) / 2)
        seg_tree[index]  = init_tree(seg_tree, given_list, index * 2 + 1, start, mid) + init_tree(seg_tree, given_list, index * 2 + 2, mid + 1, end)
    return seg_tree[index]

def seg_sum(seg_tree, index, left, right, start, end):
    # seg_Tree 에서 start ~ end 까지의 부분합을 구하기 위해 left ~ right 범위를 가지는 index에서 계산
    # 겹치지 않는 경우
    if end < left or start > right:
        return 0
    # 구하고자 하는 구간 합의 범위 내에 포함되는 경우
    elif start <= left and right <= end:
        return seg_tree[index]
    # 구하고자 하는 구간 합의 범위와 겹치는 경우
    else:
        mid = int((left + right) / 2)
        return seg_sum(seg_tree, index * 2 + 1, left, mid, start, end) + seg_sum(seg_tree, index * 2 + 2, mid + 1, right, start, end)

def seg_update(seg_tree, index, start, end, updateIndex, diff):
    # 기존의 배열에서 update 할 index ( updateIndex ) 를 통해 seg_tree의 값을 변경
    # diff 만큼 값이 변경 됐을때의 값을 Update.
    if end < updateIndex or updateIndex < start:
        return;
    seg_tree[index] += diff
    if start != end:
        mid = int((start + end) / 2)
        seg_update(seg_tree, index * 2 + 1, start, mid, updateIndex, diff)
        seg_update(seg_tree, index * 2 + 2, mid + 1, end, updateIndex, diff)

if __name__ == "__main__":
    given_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    N = len(given_list)
    add_up_list = add_up_dp(given_list, N)

    print(get_add_total(add_up_list, 4, 5))
    
    seg_tree = make_seg_tree(given_list, N)
    print(seg_sum(seg_tree, 0, 0, N, 0, N))
    print(seg_tree)
    seg_update(seg_tree, 0, 0, N, 0, 10)
    print(seg_tree)
    print(seg_sum(seg_tree, 0, 0, N, 0, N))