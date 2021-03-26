import sys

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    K = int(inp[0])
    N = int(inp[1])
    M = int(inp[2])

    if K * N < M:
        print(0)
    else:
        print(K * N - M)
