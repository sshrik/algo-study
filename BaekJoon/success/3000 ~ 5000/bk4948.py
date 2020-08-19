# Calc primeNumber n to 2n
def isPrime(prime, N):
    rl = int(len(prime) ** 0.5) + 1
    for i in range(0, len(prime)):
        if N % prime[i] == 0:
            return False
        if i > rl:
            break
    return True

def calcPrime(pnList, n):
    return pnList[2 * n - 1] - pnList[n]

MAX_NUM = 123457 * 2

numList = list(range(1,MAX_NUM + 1))
l = len(numList)

primeList = []
primeNumberList = [0]
primeNumber = 0

for i in range(1, l):
    if isPrime(primeList, numList[i]):
        primeNumber += 1
        primeList.append(numList[i])
    primeNumberList.append(primeNumber)

while True:
    inp = int(input())
    if inp == 0:
        break
    else:
        #print(calcPrime(primeNumberList, inp))
        cnt = 0
        for i in range(0, len(primeList)):
            if primeList[i] > inp and primeList[i] <= inp * 2:
                cnt += 1
            if primeList[i] > inp * 2 + 1:
                break
        print(cnt)
    