
def longest_common_substring(str1, str2):
    LCS = [[0 for _ in range(0, len(str2) + 1)] for _ in range(0, len(str1) + 1)]

    ans = 0
    ans_location = []
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
                if ans < LCS[i][j]:
                    ans = LCS[i][j]
                    ans_location = [(i, j)]
                elif ans == LCS[i][j]:
                    ans_location.append((i, j))

    return ans, get_longest_common_substring(LCS, ans_location, str1, str2)

def get_longest_common_substring(LCS, ans_location, str1, str2):
    x = len(LCS) - 1
    y = len(LCS[0]) - 1

    ret_value = []

    for i in range(0, len(ans_location)):
        answer = ""
        x = ans_location[i][0]
        y = ans_location[i][1]
        while LCS[x][y] != 0:
            answer = str1[x - 1] + answer
            x -= 1
            y -= 1
        ret_value.append(answer)

    return ret_value
            

    while x != 0 and y != 0:
        # 같을 때 Queue 에 추가해서 재귀로 돌린다면 모든 최장 길이의 공통 문자열을 찾을 수 있다. ( Backtracking으로 )
        if LCS[x][y] == LCS[x-1][y]:
            x -= 1
        elif LCS[x][y] == LCS[x][y-1]:
            y -= 1
        else:
            ret_value = str1[x - 1] + ret_value
            x -= 1
            y -= 1
    return ret_value

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

    return ans, get_longest_common_subsequence(LCS, str1, str2)

def get_longest_common_subsequence(LCS, str1, str2):
    x = len(LCS) - 1
    y = len(LCS[0]) - 1

    ret_value = ""
    print(LCS)

    while x != 0 and y != 0:
        # 같을 때 Queue 에 추가해서 재귀로 돌린다면 모든 최장 길이의 공통 문자열을 찾을 수 있다. ( Backtracking으로 )
        if LCS[x][y] == LCS[x-1][y]:
            x -= 1
        elif LCS[x][y] == LCS[x][y-1]:
            y -= 1
        else:
            ret_value = str1[x - 1] + ret_value
            x -= 1
            y -= 1
    return ret_value

if __name__ == "__main__":
    print(longest_common_subsequence("ABCED", "BCEDF"))
