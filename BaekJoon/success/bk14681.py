import sys

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    x = int(sys.stdin.readline().rstrip())
    y = int(sys.stdin.readline().rstrip())
    if x > 0:
        if y > 0:
            print(1)
        else:
            print(4)
    else:
        if y > 0:
            print(2)
        else:
            print(3)