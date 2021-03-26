# https://www.acmicpc.net/problem/5014
import sys

NOT_VISITED = -1

def check_next_step(count, count_stack, now, up, down, max_floor):
    if now + up < max_floor + 1:
        if count[now + up] == NOT_VISITED:
            count[now + up] = count[now] + 1
            count_stack.append(now + up)
    if now - down > 0:
        if count[now - down] == NOT_VISITED:
            count[now - down] = count[now] + 1
            count_stack.append(now - down)

if __name__ == "__main__":
    inp = sys.stdin.readline().split(" ")
    F = int(inp[0]) # 최대
    S = int(inp[1]) # 시작
    G = int(inp[2]) # 목표
    U = int(inp[3]) # 위로 U층만큼 이동
    D = int(inp[4]) # 아래로 D층만큼 이동

    count = [NOT_VISITED for _ in range(F + 1)]
    count[S] = 0
    # 만약 a-u > 0 and a + D < F + 1
    # count[a] =  min(count[a - U], count[a + D])
    count_stack = []
    check_next_step(count, count_stack, S, U, D, F)

    while count_stack:
        now = count_stack[0]
        del count_stack[0]
        check_next_step(count, count_stack, now, U, D, F)
        if count[G] != NOT_VISITED:
            break

    if count[G] == NOT_VISITED:
        print("use the stairs")
    else:
        print(count[G])
    