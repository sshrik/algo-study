# https://www.acmicpc.net/problem/4299


import sys

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    score_sum = int(inp[0])
    score_sub = int(inp[1])
    
    if ( score_sum + score_sub ) % 2 == 1:
        print(-1)
    elif score_sub == 0 and score_sum == 0:
        print("0 0")
    elif score_sub >= score_sum:
        print(-1)
    else:
        print(int((score_sum + score_sub) / 2), int((score_sum - score_sub) / 2))

