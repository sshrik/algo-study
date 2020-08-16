import sys

NOW_CHANNEL = 100
CHANNEL_MAX = 500000

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    avail_list = [i for i in range(0, 10)]
    if M != 0:
        inp = sys.stdin.readline().rstrip().split(" ")
    else:
        inp = []

    for i in range(0, len(inp)):
        del avail_list[avail_list.index(int(inp[i]))]

    only_plus_minus = N - NOW_CHANNEL if N > NOW_CHANNEL else NOW_CHANNEL - N

    if M == 10:
        print(only_plus_minus)
    elif N == 100:
        print(0)
    else:
        # 사용 가능한 숫자로 만든 조합중에서 가장 차이가 적은걸 쓰면 될 것 같다.
        dec_all_list = []
        dec_list = [[[str(a)] for a in avail_list]]
        dec_all_list = [str(a) for a in avail_list]

        n = 1 # n 은 n + 1의 자릿수를 의미한다.
        while n < len(str(N)) + 1:
            # 사용 가능한 숫자로 조합을 만듬.
            dec_list.append([[] for _ in avail_list])

            for i in range(0, len(avail_list)):
                for j in range(0, len(avail_list)):
                    dec_list[n][i] += [str(avail_list[i]) + contents for contents in dec_list[n-1][j]]
                dec_all_list += dec_list[n][i]
            n += 1
        
        pivot = 0
        for i in range(0, len(dec_all_list)):
            if int(dec_all_list[i]) > N:
                pivot = i
                break

        try:
            print(dec_all_list[pivot])
            print(dec_all_list[pivot - 1])
        except:
            pass
        digit_same_num = int(dec_all_list[pivot])   # Larger number then given N.
        digit_same = len(dec_all_list[pivot])
        if pivot != 0:
            digit_small_num = int(dec_all_list[pivot - 1])  # Smaller number then given N.
            digit_small = len(dec_all_list[pivot - 1])
            
            btn_touch1 = digit_same
            btn_touch1 += N - digit_same_num if N > digit_same_num else digit_same_num - N

            btn_touch2 = digit_small
            btn_touch2 += N - digit_small_num if N > digit_small_num else digit_small_num - N
            if btn_touch1 < btn_touch2:
                print(btn_touch1 if btn_touch1 < only_plus_minus else only_plus_minus)
            else:
                print(btn_touch2 if btn_touch2 < only_plus_minus else only_plus_minus)
        else:
            btn_touch = digit_same
            btn_touch += N - digit_same_num if N > digit_same_num else digit_same_num - N
            print(btn_touch if btn_touch < only_plus_minus else only_plus_minus)