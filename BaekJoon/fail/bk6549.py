# https://www.acmicpc.net/problem/6549
import sys
from collections import deque
fastio = sys.stdin.readline

def get_next_step(h_list, now, max_list, max_width):
    # 현재 now index에서 다음 index로 갈 때 다음 step의 나올 직사각형 곱을 구함.
    next_max_list = deque()
    next_max_width = deque()

    if h_list[now] <= h_list[now + 1]:
        for i in range(len(max_list)):
            next_max_list.append(max_list[i])
            next_max_width.append(max_width[i] + 1)
    else:
        for i in range(len(max_list)):
            next_max_list.append(min([h_list[now + 1], max_list[i]]))
            next_max_width.append(max_width[i] + 1)

    next_max_list.append(h_list[now + 1])
    next_max_width.append(1)
    return reduce_list(next_max_list, next_max_width)

def reduce_list(max_list, width_list):
    i = 0
    while i < len(max_list) - 1:
        if max_list[i] == max_list[i + 1]:
            del max_list[i + 1]
            del width_list[i + 1]
        else:
            i += 1
    return max_list, width_list

def get_max_multiply(max_list, width_list):
    max_val = -1

    for i in range(len(max_list)):
        temp = max_list[i] * width_list[i]
        if max_val < temp:
            max_val = temp
    
    return max_val

if __name__ == "__main__":
    while True:
        inp = fastio().rstrip()
        if len(inp) == 1 and inp[0] == "0":
            break

        inp = inp.split(" ")
        h_list = []
        for i in inp[1:]:
            h_list.append(int(i))
        h_list = deque(range(1, 10000))
        
        max_list = deque([h_list[0]])
        width_list = deque([1])
        
        max_multiply = get_max_multiply(max_list, width_list)

        for i in range(0, len(h_list) - 1):
            # print(max_list, width_list)
            max_list, width_list = get_next_step(h_list, i, max_list, width_list)
            temp = get_max_multiply(max_list, width_list)
            if temp > max_multiply:
                max_multiply = temp
        
        print(max_multiply)
        