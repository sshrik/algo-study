def getGCD(num1, num2):
    if num1 < num2:
        # Swap
        temp = num1
        num1 = num2
        num2 = temp

    while num1 % num2 != 0:
        num1 = num1 % num2
        # Swap
        temp = num1
        num1 = num2
        num2 = temp
    return num2

def getLCM(num1, num2):
    return int(num1 * num2 / getGCD(num1, num2))

def getYear(n1, n2, n3, n4):
    '''
    n1 : M / n2 : N / n3 : x / n4 : y
    x / y == n % M + 1 / n % N + 1
    a - 1, b - 1 = n % M, n % N
    M * i + a == N * j + b 가 같아질 때 n 은 그 값에 + 1 ( 다만 최소공배수보단 작거나 같아야함. ) => n1 * i + n3 == n2 * j + n4
    '''
    lcm = getLCM(n1, n2)
    res1 = n3
    res2 = n4
    
    while True:
        if res1 > lcm or res2 > lcm:
            return -1
        elif res1 == res2:
            return res1
        elif res1 > res2:
            res2 += n2
        elif res1 < res2:
            res1 += n1

T = int(input())
for t in range(0, T):
    inp = input().split(" ")
    M = int(inp[0])
    N = int(inp[1])
    x = int(inp[2])
    y = int(inp[3])
    print(getYear(M, N, x, y))



