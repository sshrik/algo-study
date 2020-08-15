n, k = map(int,input().split())

div = 1000000007

bc = []
for i in range(0, n+1):
    bc.append([])
    for j in range(0, n+1):
        bc[i].append([])

for i in range(0, n+1):
    bc[i][0] = 1
    bc[i][i] = 1

for i in range(2, n+1):
    for j in range(1, i):
        bc[i][j] = (bc[i-1][j-1] + bc[i-1][j]) % div

print(bc[n][k])
