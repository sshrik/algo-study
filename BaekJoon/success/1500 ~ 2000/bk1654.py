# https://www.acmicpc.net/problem/1654
import sys
fastio = sys.stdin.readline


def check_count(num_list, dest, N):
    count = 0
    for k in num_list:
        count += k // dest
    
    return count

if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    K = int(inp[0])
    N = int(inp[1])

    num_list = []
    for _ in range(K):
        num_list.append(int(fastio().rstrip()))
    
    max_num = max(num_list)
    min_num = 1

    while max_num >= min_num:
        mid = (max_num + min_num) // 2
        # print(max_num, mid, min_num)
        count = check_count(num_list, mid, N)
        if count >= N:
            min_num = mid + 1
            if mid > max_num:
                max_num = mid
        elif count < N:
            max_num = mid - 1
    
    print(max_num)

