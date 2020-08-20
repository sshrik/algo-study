import sys

def lis2(sequence, N):
    # sequence : 주어진 수열. 1차원 리스트의 형태이다. 최소 1개 이상임을 보장.
    D = [1 for _ in range(0, N)]

    for i in range(1, N):
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                if D[i] < D[j] + 1:
                    D[i] = D[j] + 1
    
    return max(D)

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    seq = []
    inp = sys.stdin.readline().rstrip().split(" ")
    for c in inp:
        seq.append(int(c))
    print(lis2(seq, N))


'''
6
10 20 10 30 20 50
=> 4

4
1 1 1 1 
=> 1

10
4 3 4 3 2 1 4 5 6 2
=> 4

10
5 4 5 6 5 5 7 10 2 10
=> 5

6
5 6 7 1 2 4
=> 3

11
4 1 4 1 5 6 2 3 4 7 8
=> 6

'''