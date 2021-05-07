# https://www.acmicpc.net/problem/1011
import sys
fastio = sys.stdin.readline

def get_count(N):
    now_add = 1
    total = 0
    count = 0

    while True:
        #print(N, total, count, now_add)
        if total + now_add * 2 >= N:
            if total + now_add < N:
                return count + 2
            else:
                return count + 1
        total += now_add * 2
        now_add += 1
        count += 2

if __name__ == "__main__":
    T = int(fastio().rstrip())
    
    for t in range(T):
        inp = fastio().rstrip().split(" ")
        N = int(inp[1]) - int(inp[0])
        print(get_count(N))



