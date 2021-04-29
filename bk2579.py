# https://www.acmicpc.net/problem/2579
import sys
fastio = sys.stdin.readline

def check_continued_stair(before_stack):
    if len(before_stack) == 0:
        return 0
    elif len(before_stack) == 1:
        return 1
    else:
        if before_stack[-1][0] == before_stack[-2][0] + 1:
            return 2
        else:
            return 1

def get_candidate(N, i, before_stack):
    # N 번째 계단까지 있을 때, 다음으로 갈 수 있는 곳의 목록.
    ccs = check_continued_stair(before_stack)
    if ccs == 0 or ccs == 1:
        if i + 1 <= N:
            if i + 2 <= N:
                return [i + 1, i + 2]
            else:
                return [i + 1]
    else:
        if i + 2 <= N:
            return [i + 2]
    return []

def get_score(before_stack, stair):
    score = 0
    for s in range(len(before_stack)):
        score += stair[before_stack[s][0]]
    return score

if __name__ == "__main__":
    N = int(fastio().rstrip())
    stair = []

    for _ in range(N):
        stair.append(int(fastio().rstrip()))
    
    # score[i][0] : i 번째 계단을 밟지 않을 때 최대 점수 = max(score[i - 1][1], score[i - 1][2])
    # score[i][1] : i 번째 계단을 첫번째로 밟을 때 최대 점수 = max(score[i - 1][0] + stair[i], score[i - 2][1] + stair[i], score[i - 2][2] + stair[i])
    # score[i][2] : i 번째 계단을 두번째로 밟을 때 최대 점수 = score[i - 1][1] + stair[i]
    score = [[0 for _ in range(3)] for _ in range(N)]

    if N == 1:
        print(stair[0])
    elif N == 2:
        print(stair[0] + stair[1])
    else:
        score[0][1] = stair[0]
        score[1][0] = score[0][1]
        score[1][1] = stair[1]
        score[1][2] = stair[0] + stair[1]

        for i in range(2, N):
            score[i][0] = max(score[i - 1][1], score[i - 1][2])
            score[i][1] = max(score[i - 1][0] + stair[i], score[i - 2][1] + stair[i], score[i - 2][2] + stair[i])
            score[i][2] = score[i - 1][1] + stair[i]

        print(max(score[N-1][1], score[N-1][2]))


