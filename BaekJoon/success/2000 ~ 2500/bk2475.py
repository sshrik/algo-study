import sys

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")

    dec = 0
    for i in range(0, len(inp)):
        dec += int(inp[i]) ** 2
    print(dec % 10)