import sys
import itertools

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])
    S = int(inp[1])
    answer = 0

    numbers = []
    inp = sys.stdin.readline().rstrip().split(" ")
    for i in inp:
        numbers.append(int(i))
    
    comb = []
    for n in range(1, N + 1):
        comb += itertools.combinations(numbers, n)

    for c in comb:
        if sum(c) == S:
            answer += 1

    print(answer)