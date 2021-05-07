# https://www.acmicpc.net/problem/1927
import heapq
import sys
fastio = sys.stdin.readline


if __name__ == "__main__":
    T = int(fastio().rstrip())
    heap = []

    for t in range(T):
        N = int(fastio().rstrip())
        if N == 0:
            if len(heap) == 0:
                print(0)
            else:
                res = heapq.heappop(heap)
                print(res)
        else:
            heapq.heappush(heap, N)
