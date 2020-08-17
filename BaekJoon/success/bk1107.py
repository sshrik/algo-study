import sys

NOW_CHANNEL = 100
CHANNEL_MAX = 1000000   # 500,000 가 최대지만, 그보다 높은 수가 나올 수 있기 떄문에 1,000,000을 최대로 한다.

def check_makable(N, broken_list):
    str_N = str(N)

    # N 을 구성하는 모든 수가 가능한 리스트에 있는지 확인.
    for n in str_N:
        if broken_list[int(n)]:
            return False
    
    return True

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    N = int(sys.stdin.readline().rstrip())
    M = int(sys.stdin.readline().rstrip())
    broken_list = [False for _ in range(0, 10)]

    if M != 0:
        inp = sys.stdin.readline().rstrip().split(" ")
        for i in inp:
            broken_list[int(i)] = True

    if N >= 10:
        low_bound = 10 ** (len(str(N)) - 2)
        upper_bound = 10 ** len(str(N))
    else:
        low_bound = 0
        upper_bound = 100
    
    # Low, Upper bound 를 쓰는 방식은 오류가 있다고 한다. 이유는 왤까?
    print(" ==== ")
    print(low_bound)
    print(upper_bound)
    print(N)
    print(" ==== ")

    min_answer = abs(100 - N)

    for n in range(0, CHANNEL_MAX):
        if check_makable(n, broken_list):
            # 만약 만들 수 있는 숫자라면 버튼 누르는 횟수 계산.
            answer = len(str(n)) + abs(n - N)
            if answer < min_answer:
                min_answer = answer

    print(min_answer)
    

# 이하는 실패했던 코드들.

import sys

NOW_CHANNEL = 100
CHANNEL_MAX = 500000
'''
에러인 경우는 아래가 있다.
1. digit 에서 차이가 나는 경우.
    ex ) 1555 [0, 1, 3, 4, 5, 6, 7, 9] => 888 과 2222를 통해 비교 하면 됨.
    ex ) 162 [0, 1, 3, 4, 5, 6, 7, 8, 9] => 22 랑 222를 통해 비교 하면 됨.
2. + 와 - 만 누르는게 더 빠른 경우
    ex ) 101 같은 경우
3. 0에서 시작 혹은 100에서 시작해서 내렸다가 올렸다 하는게 더 빠른 경우.
    ex ) 10 [1, 2, 3, 4, 5, 6, 7, 8, 9] => 0 에서 시작 혹은 100에서 시작.
4. 버튼을 모두 쓰거나 모두 못쓰는 경우.
'''


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
    elif M == 0:
        print(len(str(N)))
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
        
        # 가능성 있는 숫자를 찾아낸다. 
        # Upper bound 를 쓰면 더 빠르게 찾을 수 있긴 하지만, 50만개는 적은 수라 그대로 둬도 상관 없을듯.
        pivot = 0
        for i in range(0, len(dec_all_list)):
            if int(dec_all_list[i]) > N:
                pivot = i
                break

        # 같은 자릿수와 한 자릿수 더 작은 수를 비교.
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
            btn_touch = digit_sameㅉ
            btn_touch += N - digit_same_num if N > digit_same_num else digit_same_num - N
            print(btn_touch if btn_touch < only_plus_minus else only_plus_minus)