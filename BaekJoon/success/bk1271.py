import sys

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")
    n = int(inp[0]) # Money
    m = int(inp[1]) # Creature Number

    print(n // m)
    print(n % m)