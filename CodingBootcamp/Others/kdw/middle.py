# 3-2. 정렬된 두 배열의 중앙값
# 입력 예시
# 1 2
# 3 4
first = list(map(int, input().split()))
second = list(map(int, input().split()))

m = len(first)
n = len(second)

if m > n:
    first, second = second, first
    m, n = n, m

mini = 0
maxi = m
half = (m + n + 1) // 2

while mini <= maxi:
    i = (mini + maxi) // 2
    j = half - i
    if i < maxi and second[j - 1] > first[i]:
        mini = i + 1
    elif i > mini and first[i - 1] > second[j]:
        maxi = i - 1
    else:
        left = 0
        if i == 0:
            left = second[j - 1]
        elif j == 0:
            left = first[i - 1]
        else:
            left = max(first[i - 1], second[j - 1])
        if (m + n) % 2 == 1:
            print(left)
            break
        right = 0
        if i == m:
            right = second[j]
        elif j == n:
            right = first[i]
        else:
            right = min(second[j], first[i])
        print((left + right) / 2)
        break
