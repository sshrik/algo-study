import sys

def longest_common_subsequence(str1, str2):
    LCS = [[0 for _ in range(0, len(str2) + 1)] for _ in range(0, len(str1) + 1)]

    ans = 0
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
                if ans < LCS[i][j]:
                    ans = LCS[i][j]
            else:
                LCS[i][j] = LCS[i - 1][j] if LCS[i - 1][j] > LCS[i][j - 1] else LCS[i][j - 1]

    return ans

if __name__ == "__main__":
    str1 = sys.stdin.readline().rstrip()
    str2 = sys.stdin.readline().rstrip()

    print(longest_common_subsequence(str1, str2))