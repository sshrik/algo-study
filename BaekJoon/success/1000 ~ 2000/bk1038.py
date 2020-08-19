import sys

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    N = int(sys.stdin.readline().rstrip())
    dec_list = [[[str(i)] for i in range(0, 10)]]
    dec_all_list = [str(i) for i in range(0, 10)]

    if N > 1022:
        print(-1)
    elif N == 1022:
        print(9876543210)
    else:
        n = 1   # n 은 n+1의 자릿수를 의미
        while len(dec_all_list) < 1023:
            dec_list.append([[] for _ in range(0, 10)])

            for i in range(1, 10):
                for j in range(0, i):
                    dec_list[n][i] += [str(i) + contents for contents in dec_list[n-1][j]]
                dec_all_list += dec_list[n][i]
            n += 1

        print(dec_all_list[N]) 