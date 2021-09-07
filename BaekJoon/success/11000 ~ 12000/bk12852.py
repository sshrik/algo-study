# https://www.acmicpc.net/problem/12852
import sys
from collections import deque
fastio = sys.stdin.readline

DEST_NUM = 1

def make_one(N):
    bfs_queue = deque([(N, 0, [N])])

    while bfs_queue:
        now = bfs_queue.popleft()
        now_num = now[0]
        now_step = now[1]
        now_steps = now[2]

        if now_num == DEST_NUM:
            return now_step, now_steps
        
        if now_num % 2 == 0:
            next_num = int(now_num // 2)
            bfs_queue.append((next_num, now_step + 1, now_steps + [next_num] ))
        if now_num % 3 == 0:
            next_num = int(now_num // 3)
            bfs_queue.append((next_num, now_step + 1, now_steps + [next_num]))
        bfs_queue.append((now_num - 1, now_step + 1, now_steps + [now_num - 1]))

def make_onecount(N):
    onecount = [0 for _ in range(N + 1)]
    one_count_list = [deque([i]) for i in range(N + 1)]
    onecount[2] = 1
    one_count_list[2].append(1)
    onecount[3] = 1
    one_count_list[3].append(1)

    for i in range(4, N + 1):
        dest = deque()
        if i % 3 == 0:
            dest.append((onecount[int(i // 3)] + 1, int(i // 3)))
        if i % 2 == 0:
            dest.append((onecount[int(i // 2)] + 1, int(i // 2)))
        dest.append((onecount[i - 1] + 1, i - 1))

        min_count, min_num = min(dest)
        onecount[i] = min_count
        one_count_list[i].append(min_num)

    return onecount, one_count_list

if __name__ == "__main__":
    N = int(fastio())

    if N == 1:
        print(0)
        print("1")
    elif N == 2:
        print(1)
        print("2 1")
    else:
        number_count, number_steps = make_onecount(N)

        print(number_count[N])

        next_number = N
        while next_number != 1:
            print(number_steps[next_number][0], end=" ")
            next_number = number_steps[next_number][1]
        print(1)