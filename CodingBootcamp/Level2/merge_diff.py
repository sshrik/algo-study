# [1, 3], [2, 6], [8, 10], [15, 18]의 범위들이 입력됨.
# 1 ~ 18 중에서 한번이라도 겹쳐지는 부분을 찾아내야 한다.
# [1, 6], [8, 10], [15, 18]

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    input_set = []
    for _ in range(0, n):
        inp = sys.stdin.readline().rstrip().split(" ")
        input_set.append((int(inp[0]), int(inp[1])))    # Add diff set.
        