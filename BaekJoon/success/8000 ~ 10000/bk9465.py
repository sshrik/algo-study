# https://www.acmicpc.net/problem/9465
import sys
fastio = sys.stdin.readline

def get_max_score(N, score):
    if N == 1:
        return max(score[0][0], score[1][0])
    elif N == 2:
        return max(score[0][0] + score[1][1], score[1][0] + score[0][1])
    max_score = [[0 for _ in range(N)] for _ in range(2)]
    max_score[0][0] = score[0][0]
    max_score[1][0] = score[1][0]
    max_score[0][1] = score[0][1] + max_score[1][0]
    max_score[1][1] = score[1][1] + max_score[0][0]

    for n in range(2, N):
        max_score[0][n] = score[0][n] + max(max_score[1][n - 1], max_score[1][n - 2])
        max_score[1][n] = score[1][n] + max(max_score[0][n - 1], max_score[0][n - 2])
    
    return max(max_score[0][-1], max_score[0][-2], max_score[1][-1], max_score[1][-2])

if __name__ == "__main__":
    T = int(fastio().rstrip())

    for t in range(T):
        N = int(fastio().rstrip())
        score = [[], []]
        for i in range(2):
            inp = fastio().rstrip().split(" ")
            for j in inp:
                score[i].append(int(j))
        print(get_max_score(N, score))

