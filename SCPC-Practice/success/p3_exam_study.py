import sys

T = int(sys.stdin.readline().rstrip())  # For fast I / O. T mean test case number.
for t in range(0, T):
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])
    K = int(inp[1])
    score = []

    inp = sys.stdin.readline().rstrip().split(" ")
    for i in range(0, N):
        score.append(int(inp[i]))
    
    score.sort()

    max_score = 0
    for i in range(0, K):
        max_score += score[N - i - 1]
    
    print("Case #" + str(t + 1))
    print(max_score)
