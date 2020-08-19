N = int(input())

A = []
B = []

inpA = input().split(" ")
inpB = input().split(" ")

for i in range(0, N):
    A.append(int(inpA[i]))
    B.append(int(inpB[i]))

A.sort()
B.sort()

res = 0
for i in range(0, N):
    res += A[i] * B[N - i - 1]

print(res)