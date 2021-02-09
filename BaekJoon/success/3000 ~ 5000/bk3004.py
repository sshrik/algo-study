# https://www.acmicpc.net/problem/3004


import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    
    ans = 0

    if n % 2 == 0:
        halfn = int(n/2)
        ans = (halfn + 1) * (halfn + 1)
    else:
        halfn = int((n + 1)/2)
        ans = (halfn + 1) * (halfn)
    
    print(ans)