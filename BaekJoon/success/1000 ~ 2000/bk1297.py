# https://www.acmicpc.net/problem/1297


import sys
import math

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    d = int(inp[0])
    h = int(inp[1])
    w = int(inp[2])

    dd = d * d
    hh = h * h
    ww = w * w

    rh = dd * hh / ( ww + hh )
    rw = dd * ww / ( ww + hh )

    print(int(math.sqrt(rh)), int(math.sqrt(rw)))
