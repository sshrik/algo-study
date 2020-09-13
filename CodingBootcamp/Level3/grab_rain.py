# 0 1 0 2 1 0 1 3 2 1 2 1 의 지형을 배열로 나타낸 것은
# 각각의 위치의 높이이다. 이 때, 담길 수 있는 물의 양을 채워보자.

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    height_list = []

    for _ in range(0, n):
        height_list.append(int(sys.stdin.readline().rstrip()))
    
