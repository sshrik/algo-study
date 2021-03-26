import sys

def get_next(arr, now, K):
    next_idx = ( now + K - 1 ) % len(arr)
    print(arr[next_idx], end="")
    del arr[next_idx]
    return next_idx

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0]) # How many people
    K = int(inp[1])
    circle_list = [i for i in range(1, N + 1)]
    now = 0

    print("<", end="")
    while True:
        now = get_next(circle_list, now, K)
        if len(circle_list) != 0:
            print(", ", end="")
        else:
            print(">")
            break
