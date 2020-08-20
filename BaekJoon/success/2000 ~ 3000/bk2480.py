import sys

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    A = int(inp[0])
    B = int(inp[1])
    C = int(inp[2])

    prize = 0

    if A == B == C:
        prize = A * 1000 + 10000
    elif A == B or A == C:
        prize = A * 100 + 1000
    elif B == C:
        prize = B * 100 + 1000
    else:
        prize = max([A, B, C]) * 100
    
    print(prize)