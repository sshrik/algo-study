# P(N) = P(N-2) + P(N-3), Start with 1 1 1
P = [1, 1, 1]
i = 3

while len(P) < 101:
    P.append(P[i - 2] + P[i - 3])
    i += 1

N = int(input())
for _ in range(0, N):
    print(P[int(input()) - 1])