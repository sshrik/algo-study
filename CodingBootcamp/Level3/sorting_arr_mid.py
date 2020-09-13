# O(log (m + n))안에서 두개의 정렬된 배열의 중간 값을 반환하라.
# m, n 은 1000 이하이고, 각각은 -10^6 ~ 10^6 사이의 숫자.
import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstirp())
    n_list = []
    for _ in range(0, n):
        n_list.append(int(sys.stdin.readline().rstirp()))
    
    m = int(sys.stdin.readline().rstirp())
    m_list = []
    for _ in range(0, n):
        m_list.append(int(sys.stdin.readline().rstirp()))