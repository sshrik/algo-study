# https://www.acmicpc.net/problem/12865
import sys
fastio = sys.stdin.readline



if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    K = int(inp[1])

    weight_list = []
    value_list = []

    for n in range(N):
        inp = fastio().rstrip().split(" ")
        W = int(inp[0])
        V = int(inp[1])
        weight_list.append(W)
        value_list.append(V)

    dp = [[0] * (N + 1) for _ in range(K + 1)]

    for k in range(1, K+1):
        max_value = 0
        for n in range(1, N + 1):
            if weight_list[n - 1] > k:
                dp[k][n] = dp[k][n - 1]
            else:
                dp[k][n] = max([value_list[n - 1] + dp[k - weight_list[n - 1]][n - 1], dp[k][n - 1]])

    print(max(dp[-1]))
