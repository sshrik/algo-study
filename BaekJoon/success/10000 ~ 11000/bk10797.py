import sys

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    day = int(sys.stdin.readline().rstrip()) % 10
    inp = sys.stdin.readline().rstrip().split(" ")
    
    ans = 0
    for i in range(0, len(inp)):
        if int(inp[i]) % 10 == day:
            ans += 1
    print(ans)