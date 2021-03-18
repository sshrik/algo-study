# https://www.acmicpc.net/problem/5575
import sys

fastio = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(3):
        inp = fastio().split(" ")
        startH = int(inp[0])
        startM = int(inp[1])
        startS = int(inp[2])
        endH = int(inp[3])
        endM = int(inp[4])
        endS = int(inp[5])

        duringH = 0
        duringM = 0
        duringS =  endS - startS
        if duringS < 0:
            duringM -= 1
            duringS += 60

        duringM = endM - startM + duringM
        if duringM < 0:
            duringH -= 1
            duringM += 60
        
        duringH = endH - startH + duringH
    
        print(duringH, duringM, duringS)
