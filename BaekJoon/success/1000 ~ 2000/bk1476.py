import sys

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")
    E = int(inp[0])
    S = int(inp[1])
    M = int(inp[2])

    N = 1
    while True:
        if (N - E) % 15 == 0:
            if (N - S) % 28 == 0:
                if (N - M) % 19 == 0:
                    print(N)
                    break
        N += 1
