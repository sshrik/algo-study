import sys

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])
    M = int(inp[1])

    print(abs(N - M))