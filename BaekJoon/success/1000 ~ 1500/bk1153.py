# https://www.acmicpc.net/problem/1153

import math
def is_prime(n, prime):
    if prime[n] == True:
        return True
    elif prime[n] == False:
        return False
    
    sqrtn = math.ceil(n ** 0.5)
    if n == 1 or n == 0:
        return False

    for p in range(2, sqrtn + 1):
        if n % p == 0:
            prime[n] = False
            return False
    prime[n] = True
    return True

def can_make_with_prime(n, prime):
    half_n = math.ceil(n / 2)
    for i in range(half_n, 1, -1):
        if is_prime(i, prime):
            if is_prime(n - i, prime):
                return True, (i , n-i)
    return False, (-1, -1)

def calc_four_prime(n):
    prime = [-1] * (n + 1)
    check_prime(n, prime)
    # print(prime)

    half_n = math.ceil(n / 2)
    
    for i in range(4, half_n + 1):
        res1, ans1 = can_make_with_prime(i, prime)
        res2, ans2 = can_make_with_prime(n - i, prime)
        if res1 and res2:
            return [ans1[0], ans1[1], ans2[0], ans2[1]]

    return -1


def check_prime(n, prime):
    prime[0] = False
    prime[1] = False
    for i in range(0, n):
        if prime[i] == -1:
            prime[i] = True
            now = i + i
            while now < n + 1:
                prime[now] = False
                now += i

if __name__ == "__main__":
    n = int(input())
    
    ans = calc_four_prime(n)
    if ans == -1:
        print(-1)
    else:
        for a in ans:
            print(a, end=" ")
