# https://www.acmicpc.net/problem/9252
# 실수 1 : 출력값 오류
# 실수 2 : AEA, EAE
# 실수 3 : AA 와 AE
# 실수 4 : AAEE 와 EEAA
# 실수 5 : ADQWEQWDQWGFSDAHWREYERFGD 와 FGDGFDSGWERDSAFLSD
import sys
fastio = sys.stdin.readline

def LCS(strA, strB):
    LCS_map = [[0 for _ in range(len(strA) + 1)] for _ in range(len(strB) + 1)]

    for i in range(1, len(strB) + 1):
        for j in range(1, len(strA) + 1):
            if strB[i - 1] != strA[j - 1]:
                LCS_map[i][j] = LCS_map[i - 1][j] if LCS_map[i - 1][j] > LCS_map[i][j - 1] else LCS_map[i][j - 1]
            else:
                LCS_map[i][j] = LCS_map[i - 1][j - 1] + 1
    
    return LCS_map

def calc_str(strA, strB, LCS_map):
    answer = ""

    i = len(strB)
    j = len(strA)

    while LCS_map[i][j] != 0:
        if LCS_map[i][j] != LCS_map[i - 1][j]:
            if LCS_map[i][j] != LCS_map[i][j - 1]:
                if LCS_map[i][j] != LCS_map[i - 1][j -1]:
                    answer = strA[j - 1] + answer
                    i -= 1
                    j -= 1
            else:
                j -= 1
        else: 
            if LCS_map[i][j] != LCS_map[i][j - 1]:
                i -= 1
            else:
                if LCS_map[i][j] != LCS_map[i - 1][j -1]:
                    answer = strA[j - 1] + answer
                    i -= 1
                    j -= 1
                else:
                    i -= 1
                
    return answer

if __name__ == "__main__":
    A = fastio().rstrip()
    B = fastio().rstrip()
    LCS_map = LCS(A, B)
    # print(LCS_map)
    print(LCS_map[-1][-1])
    if LCS_map[-1][-1] != 0:
        print(calc_str(A, B, LCS_map))

'''
AWERACWEADRG
WRACSQAEG

ADQWEQWDQWGFSDAHWREYERFGD
FGDGFDSGWERDSAFLSD
'''
