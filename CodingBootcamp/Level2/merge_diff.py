# [1, 3], [2, 6], [8, 10], [15, 18]의 범위들이 입력됨. ( 작은게 앞에 온다고 가정 )
# 1 ~ 18 중에서 한번이라도 겹쳐지는 부분을 찾아내야 한다.
# [1, 6], [8, 10], [15, 18]

import sys

def merge_diff(diff1, diff2):
    small_start = diff1[0] if diff1[0] < diff2[0] else diff2[0]
    large_end = diff2[1] if diff1[1] < diff2[1] else diff1[1]

    return (small_start, large_end)

def is_contain(diff1, diff2):
    # 2개의 범위가 겹치는 부분이 있는가?
    small_start = diff1 if diff1[0] < diff2[0] else diff2
    large_start = diff2 if diff1[0] < diff2[0] else diff1
    
    return small_start[1] >= large_start[0]
    
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    input_set = []
    for _ in range(0, n):
        inp = sys.stdin.readline().rstrip().split(" ")
        input_set.append((int(inp[0]), int(inp[1])))    # Add diff set.

    input_set.sort()

    result_diff = [input_set[0]]
    