# https://www.acmicpc.net/problem/18870
import sys, heapq
fastio = sys.stdin.readline

if __name__ == "__main__":
    pq = []
    N = int(fastio().strip())
    inp = fastio().strip().split(" ")
    seq = [0 for _ in range(N)]
    numbers = []

    for n in range(N):
        numbers.append((int(inp[n]), n))
    numbers.sort()

    beforeNumber = numbers[0][0]
    numSeq = 0
    
    for n in range(N):
        if beforeNumber != numbers[n][0]:
            numSeq += 1
            beforeNumber = numbers[n][0]
        seq[numbers[n][1]] = numSeq

    for n in range(N):
        print(seq[n], end=" ")
