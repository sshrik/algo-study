N = int(input())

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    n1 = 0
    n2 = 1
    for _ in range(1, N):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print(n2)