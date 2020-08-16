import sys

T = int(sys.stdin.readline().rstrip())  # For fast I / O. T mean test case number.
for t in range(0, T):
    N = int(sys.stdin.readline().rstrip())  # N for people number.

    total_score = []    # All total score of player.

    for _ in range(0, N):
        score = int(sys.stdin.readline().rstrip())
        total_score.append(score)
    total_score.sort()
    
    max_score = -1
    for i in range(0, N):
        can_be_max = total_score[i] + N - i
        if can_be_max > max_score:
            max_score = can_be_max

    can_win = 0
    for i in range(0, N):
        if max_score <= total_score[i] + N:
            can_win += 1
    
    print("Case #" + str(t + 1))
    print(can_win)
