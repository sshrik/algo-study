import time

FIBO = 35
NOT_CALC = -1

def fibo_rec(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

def fibo_mem(n, fibo):
    if n == 1:
        fibo[n-1] = 0
        return fibo[n-1]
    elif n == 2:
        fibo[n-1] = 1
        return fibo[n-1]
    else:
        if fibo[n-1] != NOT_CALC:
            if fibo[n-2] != NOT_CALC:
                return fibo[n-1] + fibo[n-2]
            else:
                return fibo[n-1] + fibo_mem(n - 2, fibo)
        else:
            if fibo[n-2] != NOT_CALC:
                return fibo_mem(n-2, fibo) + fibo[n-2]
            else:
                return fibo_mem(n-2, fibo) + fibo_mem(n - 2, fibo)

import random

N = 200
M = 200
MAX_VALUE = N * M
MIN_PATH_LENGTH = 400

def make_random_increase_arr(N, M, max_value):
    random_arr = [random.randint(0, max_value) for _ in range(N * M)]
    random_start = random.randint(0, max_value - MIN_PATH_LENGTH - 1)
    sort_random = random_arr[random_start:random_start + MIN_PATH_LENGTH]
    sort_random.sort()
    random_arr = random_arr[0:random_start] + sort_random + random_arr[random_start + MIN_PATH_LENGTH:]
    ret_arr = [[0 for _ in range(N)] for _ in range(M)]
    for m in range(M):
        for n in range(N):
            ret_arr[m][n] = random_arr[N * m + n]
    return ret_arr

dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

VISITED = 0
NOT_VISITED = 1

def can_go(seq, x, y, d):
    return 0 <= x + dir_x[d] < len(seq[0]) and 0 <= y + dir_y[d] < len(seq)

def get_candidate(seq, x, y):
    # return candidate dir.
    ret_dir = []
    for d in range(0, 4):
        if can_go(seq, x, y, d):
            next_x = x + dir_x[d]
            next_y = y + dir_y[d]
            if seq[y][x] < seq[next_y][next_x]:
                ret_dir.append(d)
    return ret_dir

def dfs_increase_infor(seq, start_n, start_m):
    dfs_stack = [((start_n, start_m), -1, get_candidate(seq, start_n, start_m))]

    max_length = -1

    while dfs_stack:
        now = dfs_stack[-1]
        del dfs_stack[-1]

        now_x = now[0][0]
        now_y = now[0][1]
        now_cand_indx = now[1]
        now_cand = now[2]
        if now_cand_indx == len(now_cand) - 1:
            if len(dfs_stack) + 1 > max_length:
                max_length = len(dfs_stack) + 1
            continue

        now_cand_indx += 1
        dfs_stack.append(((now_x, now_y), now_cand_indx, now_cand))

        now_x += dir_x[now_cand[now_cand_indx]]
        now_y += dir_y[now_cand[now_cand_indx]]

        dfs_stack.append(((now_x, now_y), -1, get_candidate(seq, now_x, now_y)))
    
    return max_length

def find_with_dfs(arr):
    max_length = -1
    start = [(0, 0)]

    for m in range(M):
        for n in range(N):
            temp = dfs_increase_infor(arr, n, m)
            if max_length < temp:
                max_length = temp
                start = [(n, m)]
            elif max_length == temp:
                start.append((n, m))

    return max_length, start

NOT_MEMO = -1

def dfs_with_memoization(seq, start_n, start_m, memo):
    dfs_stack = [((start_n, start_m), -1, get_candidate(seq, start_n, start_m))]

    max_length = -1
    longest_stack = []

    while dfs_stack:
        now = dfs_stack[-1]
        del dfs_stack[-1]

        now_x = now[0][0]
        now_y = now[0][1]
        now_cand_indx = now[1]
        now_cand = now[2]
        
        if memo[now_y][now_x] != NOT_MEMO:
            if len(dfs_stack) + memo[now_y][now_x] > max_length:
                max_length = len(dfs_stack) + memo[now_y][now_x]
                longest_stack = [dfs_stack[i][0] for i in range(len(dfs_stack))]
                longest_stack.append((now_x, now_y))
                continue
        if now_cand_indx == len(now_cand) - 1:
            if len(dfs_stack) + 1 > max_length:
                max_length = len(dfs_stack) + 1
                longest_stack = [dfs_stack[i][0] for i in range(len(dfs_stack))]
                longest_stack.append((now_x, now_y))
            continue

        now_cand_indx += 1
        dfs_stack.append(((now_x, now_y), now_cand_indx , now_cand))

        now_x += dir_x[now_cand[now_cand_indx]]
        now_y += dir_y[now_cand[now_cand_indx]]
        
        dfs_stack.append(((now_x, now_y), -1, get_candidate(seq, now_x, now_y)))
    
    return max_length, longest_stack

def find_with_memo(arr):
    memo = [[NOT_MEMO for _ in range(N)] for _ in range(M)]

    max_length = 1
    start = [(0, 0)]

    for m in range(M):
        for n in range(N):
            temp, longest_stack = dfs_with_memoization(arr, n, m, memo)
            for ls in range(len(longest_stack)):
                now_n = longest_stack[ls][0]
                now_m = longest_stack[ls][1]
                if memo[now_m][now_n] < temp - ls:
                    memo[now_m][now_n] = temp - ls
            
            if max_length < temp:
                max_length = temp
                start = [(n, m)]
            elif max_length == temp:
                start.append((n, m))
    return max_length, start

def print_arr(arr, N, M):
    for m in range(M):
        for n in range(N):
            print(arr[m][n], end="\t")
        print("")
    
if __name__ == "__main__":
    '''
    fibo_rec(FIBO)
    print("Fibo recursive :", end - start, "s")

    start = time.time()
    fibo_mem(FIBO, [NOT_CALC for _ in range(FIBO)])
    end = time.time()
    print("Fibo memoization :", end - start, "s")
    '''
    arr = make_random_increase_arr(N, M, MAX_VALUE)
    print("Size", N, M)
    start = time.time()
    dfs_max_length, dfs_start = find_with_dfs(arr)
    end = time.time()
    print("dfs search :", end - start, "s")

    start = time.time()
    memo_max_length, memo_start = find_with_memo(arr)
    end = time.time()
    print("memo search :", end - start, "s")
    
    print(dfs_max_length == memo_max_length, dfs_max_length, memo_max_length)
    print(dfs_start, memo_start)
    #print_arr(arr, N, M)