import sys

'''
N 과 M 이 서로소인 경우를 생각 해 보자. N개의 소시지를 M 명이 먹는 경우를 생각 할 때,
N*M 길이의 소시지를 N 길이로 자르는 경우, 즉 M - 1 의 칼질을 하면 된다.
이제 a * N 과 a * M ( a 는 최대 공약수 ) 으로 생각해보면, (aN, aM) = a(N, M) 이므로, 따라서 a ( M - 1 ) 번 자르면 된다.
즉 M - gcd(M, N) 이 답이 된다.

gcd는 유클리드 알고리즘 혹은 유클리드 호제법으로 구하자.

* 위의 (aN, aM) = a(N, M) 은 N개를 M명이 나눠먹는 경우가 a 번 있다는 뜻으로 생각하면 된다.
'''

def get_times(N, M):
    # N/M 이 1/2 보다 작을경우, 소시지 하나를 얼마나 많은 N/M 조각으로 나눌 수 있는지 그 칼질 횟수를 계산.
    return M // N if M % N else (M // N) - 1

def get_gcd(N, M):
    big = N if N > M else M
    small = M if N > M else N

    while small != 0:
        temp = big % small
        big = small
        small = temp
    return big

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip().split(" ")
    N = int(inp[0])  # 소시지 갯수
    M = int(inp[1])  # 평론가 명수
    
    print( M - get_gcd(N, M) )
    