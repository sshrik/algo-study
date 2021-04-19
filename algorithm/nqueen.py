def can_put(row_a, col_a, left_up_a, right_up_a, x, y, N):
    if x > y:
        return row_a[y] and col_a[x] and left_up_a[abs(x - y) + N - 1] and right_up_a[x + y]
    else:
        return row_a[y] and col_a[x] and left_up_a[abs(x - y)] and right_up_a[x + y]

def unset_put(row_a, col_a, left_up_a, right_up_a, x, y, N):
    row_a[y] = True 
    col_a[x] = True
    if x > y:
        left_up_a[abs(x - y) + N - 1] = True
    else:
        left_up_a[abs(x - y)] = True
    right_up_a[x + y] = True 

def set_put(row_a, col_a, left_up_a, right_up_a, x, y, N):
    row_a[y] = False
    col_a[x] = False 
    if x > y:
        left_up_a[abs(x - y) + N - 1] = False
    else:
        left_up_a[abs(x - y)] = False
    right_up_a[x + y] = False 

def get_candidate(row_a, col_a, left_up_a, right_up_a, before_x, before_y, N):
    candidate = []
    for i in range(N):
        x = before_x + 1
        if can_put(row_a, col_a, left_up_a, right_up_a, x, i, N):
            candidate.append((x, i))
    return candidate

def solution(n):
    answer = 0
    # Make available.
    row_a = [True] * n
    col_a = [True] * n
    left_up_a = [True] * (2*n - 1)
    right_up_a = [True] * (2*n - 1)

    first_candidate = []
    for i in range(n):
        first_candidate.append((0, i))
        
    solution_stack = [(-1, first_candidate)]
    if n == 1:
        return 1

    while solution_stack:
        # print(solution_stack)
        if len(solution_stack) == n:
            answer += len(solution_stack[-1][1])
            del solution_stack[-1]

        now = solution_stack[-1]
        del solution_stack[-1]
        now_index = now[0]
        now_candidate = now[1]

        if now_index != -1:
            (now_x, now_y) = now_candidate[now_index]
            unset_put(row_a, col_a, left_up_a, right_up_a, now_x, now_y, n)

        if now_index == len(now_candidate) - 1:
            continue

        now_index += 1
        (now_x, now_y) = now_candidate[now_index]
        set_put(row_a, col_a, left_up_a, right_up_a, now_x, now_y, n)
        solution_stack.append((now_index, now_candidate))
        (bef_x, bef_y) = solution_stack[-1][1][solution_stack[-1][0]]

        next_cand = get_candidate(row_a, col_a, left_up_a, right_up_a, bef_x, bef_y, n)
        if len(next_cand) != 0:
            solution_stack.append((-1, next_cand))

    return answer

if __name__ == "__main__":
    for n in range(1, 12):
        print(solution(n))