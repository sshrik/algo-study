# Calc 2 x n Tile with 2x1 and 2x2 Tile.
n = int(input())

n1 = 1
n2 = 3

if n == 1:
    print(n1)
elif n == 2:
    print(n2)
else:
    for _ in range(2, n):
        n3 = (n1 * 2 + n2) % 10007
        n1 = n2
        n2 = n3
    print(n3)