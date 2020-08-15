# 0 층 : 1 2 3 4 ... 호에는 1 2 3 4 ... 명이 거주
def calcCount(N):
    # Calc 1 + 2 + .. + n
    return int(N * (N+1) / 2)

def calcFloor(PC, K, N):
    if K == 1:
        return calcCount(N)
    else:
        res = 0
        for num in range(0, N):
            res += PC[K - 1][num]
        return res

MAX_COUNT = 15

# PeopleCount[k][n] == k floor n - 1 room
peopleCount = list([list([0 for _ in range(0, MAX_COUNT)]) for _ in range(0, MAX_COUNT)])

for i in range(0, MAX_COUNT):
    peopleCount[0][i] = i + 1

for i in range(1, MAX_COUNT):
    for j in range(0, MAX_COUNT):
        peopleCount[i][j] = calcFloor(peopleCount, i, j + 1)

T = int(input())

for t in range(0, T):
    k = int(input())
    n = int(input())
    # Calc K floor n room
    print(peopleCount[k][n - 1])


