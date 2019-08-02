# Calc prime number a to b
def isPrime(prime, N):
    rl = int(len(prime) ** 0.5) + 1
    for i in range(0, len(prime)):
        if N % prime[i] == 0:
            return False
        if i > rl:
            break
    return True

# Init number.
inp = input()

a = int(inp.split(" ")[0])
b = int(inp.split(" ")[1])

if a == 1:
    if b == 1:
        exit()
    else:
        a = 2

numList = list(range(2,b + 1))
primeList = []

l = len(numList)

for i in range(0, l):
    if isPrime(primeList, numList[i]):
        primeList.append(numList[i])
for i in range(0, len(primeList)):
    if primeList[i] >= a:
        print(primeList[i])