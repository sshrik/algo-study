# B(N) = B(N-1) + B(N-2), Start with 1 2
B = [1, 2]
i = 2

while len(B) < 1000000:
    B.append((B[i-1] + B[i-2]) % 15746)
    i += 1

N = int(input())
print(B[N - 1])
