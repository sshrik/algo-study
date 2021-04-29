# https://www.acmicpc.net/problem/1931
import sys
fastio = sys.stdin.readline

def is_intersect(now_range, add_range):
    now_st = now_range[1]
    now_et = now_range[0]
    add_st = add_range[1]
    add_et = add_range[0]
    
    return now_st < add_st < now_et or now_st < add_et < now_et or add_st < now_st < add_et or add_st < now_et < add_et

def check_intersect(now_range, add_range):
    return now_range <= add_range[1]
    
if __name__ == "__main__":
    N = int(fastio().rstrip())
    sorted_time = []

    for n in range(N):
        inp = fastio().rstrip().split(" ")
        st = int(inp[0])
        et = int(inp[1])
        sorted_time.append((et, st, et - st))
    
    sorted_time.sort()

    count = 0
    now_range = -1
    for n in range(N):
        if check_intersect(now_range, sorted_time[n]):
            now_range = sorted_time[n][0]
            count += 1
    print(count)
