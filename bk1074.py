# https://www.acmicpc.net/problem/1074
import sys
fastio = sys.stdin.readline

def power_of(pow, N):
    ret_list = [1]

    for _ in range(N):
        ret_list.append(ret_list[-1] * pow)
    
    return ret_list

def get_loc(start_x, end_x, start_y, end_y, x, y):
    middle_x = int((start_x + end_x + 1) / 2)
    middle_y = int((start_y + end_y + 1) / 2)

    if start_x <= x < middle_x:
        if start_y <= y < middle_y:
            return 0, start_x, middle_x, start_y, middle_y
        else:
            return 2, start_x, middle_x, middle_y, end_y
    else:
        if start_y <= y < middle_y:
            return 1, middle_x, end_x, start_y, middle_y
        else:
            return 3, middle_x, end_x, middle_y, end_y

def get_answer(N, r, c):
    pow_2 = power_of(2, N)
    count = 0

    n = N
    start_x = 0
    end_x = pow_2[n] - 1
    start_y = 0
    end_y = pow_2[n] - 1

    while n > 1:
        loc, start_x, end_x, start_y, end_y = get_loc(start_x, end_x, start_y, end_y, c, r)
        count += pow_2[n - 1] * pow_2[n - 1] * loc
        n -= 1
        
    if c == start_x:
        if r == start_y:
            return(count + 0)
        else:
            return(count + 2)
    else:
        if r == start_y:
            return(count + 1)
        else:
            return(count + 3)


if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    r = int(inp[1])
    c = int(inp[2])

    print(get_answer(N, r, c))
    
    '''
    for r in range(0, 2 ** N):
        for c in range(0, 2 ** N):
            print(get_answer(N, r, c), end="\t")
        print("")
    '''