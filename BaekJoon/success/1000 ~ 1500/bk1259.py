# https://www.acmicpc.net/problem/1259
import sys
fastio = sys.stdin.readline

def is_palindrome(N):
    length = len(N)
    if length == 1:
        return True
    if length % 2 == 0:
        stack = N[:length//2]
        remain = N[length//2:]
    else:
        stack = N[:length//2]
        remain = N[length//2 + 1:]
    return stack == remain[::-1]

if __name__ == "__main__":
    while True:
        N = fastio().rstrip()
        if N == "0":
            break
        else:
            if is_palindrome(N):
                print("yes")
            else:
                print("no")
