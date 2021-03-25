# https://www.acmicpc.net/problem/2493
import sys
fastio = sys.stdin.readline

if __name__ == "__main__":
    N = int(fastio().rstrip())
    inp = fastio().rstrip().split(" ")
    n_list = [int(i) for i in inp]
    st = [] # (n_list[i], i) 의 Tuple 형태.

    for i in range(N):
        while len(st):
            if st[-1][0] >= n_list[i]:
                break
            else:
                del st[-1]
        if len(st) == 0:
            print("0", end=" ")
        else:
            print(st[-1][1] + 1, end=" ")     
        if len(st) != 0 and st[-1][0] == n_list[i]:
            st[-1] = (n_list[i], i)
        else:
            st.append((n_list[i], i))
    
'''
10
6 9 5 7 4 6 9 5 7 4

9
9 7 5 3 1 2 4 6 8
'''