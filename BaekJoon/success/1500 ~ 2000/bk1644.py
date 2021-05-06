# https://www.acmicpc.net/problem/1644
import sys
fastio = sys.stdin.readline
MAX_NUM = 4000000

def calc_prime(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = False
    is_prime[1] = False
    max_n = int((N + 1) ** 0.5) + 1

    for n in range(2, max_n):
        if is_prime[n] == True:
            for i in range(2 * n, N + 1, n):
                is_prime[i] = False
    
    prime_list = []
    for n in range(0, N + 1):
        if is_prime[n]:
            prime_list.append(n)
    
    return prime_list

if __name__ == "__main__":
    N = int(fastio().rstrip())
    prime_list = calc_prime(N)
    prime_length = len(prime_list)
    count = 0

    for start in range(prime_length):
        add_up = 0
        for now in range(start, prime_length):
            add_up += prime_list[now]
            if add_up > N:
                break
            elif add_up == N:
                count += 1
                break
    
    print(count)
