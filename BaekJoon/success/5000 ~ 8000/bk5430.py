# https://www.acmicpc.net/problem/5430
import sys
from collections import deque
fastio = sys.stdin.readline

def removeDq(r_val, dq):
    if r_val % 2 == 0:
        return dq.popleft()
    else:
        return dq.pop()

if __name__ == "__main__":
    T = int(fastio().rstrip())
    for t in range(T):
        r_val = 0
        f_val = fastio().rstrip()
        n = int(fastio().rstrip())
        dq = deque()
        inp = fastio().rstrip()[1:-1]
        if len(inp) != 0:
            inp = inp.split(",")
            for i in inp:
                dq.append(int(i))
        errorFlag = False
        for f in f_val:
            if f == "R":
                r_val = r_val + 1
            else:
                if len(dq) == 0:
                    errorFlag = True
                else:
                    removeDq(r_val, dq)
        if errorFlag:
            print("error")
        else:
            print("[", end="")
            while len(dq) != 0:
                print(removeDq(r_val, dq), end="")
                if len(dq) != 0:
                    print(",", end="")
            print("]")



