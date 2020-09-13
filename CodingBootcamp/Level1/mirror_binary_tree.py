# 서로 왼쪽과 오른쪽이 대칭이 된 이진트리를 만들어라
# [4, 2, 7, 1, 3, 6, 9] 를 [4, 7, 2, 9, 6, 3, 1]로

import sys

def reverse_array(arr, start, end):
    ret = []
    # 물론 arr[strat:end].reverse() 쓰면 간단하지만, : 가 arr을 복사 시켜 문제가 됨.
    for a in range(end - 1, start-1, -1):
        ret.append(arr[a])
    return ret

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    arr = []
    for _ in range(0, n):
        arr.append(int(sys.stdin.readline().rstrip()))
    # 2의 거듭제곱씩 확인하면서 2의 거듭제곱을 reverse 해서 return.
    length = 1
    before_now = 0
    reverse_arr = []
    while before_now < n:
        reverse_arr += reverse_array(arr, before_now, before_now + length)
        before_now = before_now + length
        length = length * 2
    
    for a in range(0, n):
        print(reverse_arr[a], end=" ")