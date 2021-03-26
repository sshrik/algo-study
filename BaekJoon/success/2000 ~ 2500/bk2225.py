# https://www.acmicpc.net/problem/2225
import sys

max_num = 1000000000

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0]) + 1
    K = int(inp[1]) + 1
    
    add_map = [[0 for _ in range(K)] for _ in range(N)]
    for n in range(0, N):
        add_map[n][1] = 1
    for k in range(1, K):
        add_map[0][k] = 1
        add_map[1][k] = k

    for n in range(2, N):
        for k in range(2, K):
            for i in range(0, n + 1):
                add_map[n][k] += add_map[i][k-1]
            add_map[n][k] = add_map[n][k] % max_num
                
    #print(add_map)
    print(add_map[N-1][K-1])
