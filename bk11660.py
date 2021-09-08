# https://www.acmicpc.net/problem/11660
import sys
fastio = sys.stdin.readline

def make_add_up_list(given_list, N):
    add_up_list = [[0 for _ in range(N)] for _ in range(N)]
    add_up_list[0][0] = given_list[0][0]

    for i in range(1, N):
        add_up_list[0][i] = add_up_list[0][i - 1] + given_list[0][i]
        add_up_list[i][0] = add_up_list[i - 1][0] + given_list[i][0]

    for i in range(1, N):
        for j in range(1, N):
            add_up_list[i][j] = add_up_list[i][j - 1] + add_up_list[i - 1][j] - add_up_list[i - 1][j - 1] + given_list[i][j]
    return add_up_list

def get_add_up(add_up_list, x1, y1, x2, y2):
    if x1 == 0:
        if y1 == 0:
            return add_up_list[x2][y2]
        else:
            return add_up_list[x2][y2] - add_up_list[x2][y1 - 1]
    else:
        if y1 == 0:
            return add_up_list[x2][y2] - add_up_list[x1 - 1][y2]
        else:
            return add_up_list[x2][y2] - add_up_list[x2][y1 - 1] - add_up_list[x1 - 1][y2] + add_up_list[x1 - 1][y1 - 1]


if __name__ == "__main__":
    inp = fastio().split(" ")
    N = int(inp[0])
    M = int(inp[1])
    given_list = []

    for _ in range(N):
        inp = fastio().split(" ")
        given_list.append([int(i) for i in inp])
    add_up_list = make_add_up_list(given_list, N)

    for _ in range(M):
        inp = fastio().split(" ")
        x1 = int(inp[0]) - 1
        y1 = int(inp[1]) - 1
        x2 = int(inp[2]) - 1 
        y2 = int(inp[3]) - 1
        print(get_add_up(add_up_list, x1, y1, x2, y2))
