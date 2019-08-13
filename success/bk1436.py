def getNextGen(before, digitNum):
    res = []
    for i in range(0, len(before)):
        for j in range(0, 10):
            res.append(before[i] * 10 + j)
        for j in range(1, 10):
            res.append(before[i] + j * (10 ** digitNum))
    res = list(set(res))
    res.sort()
    return res


total = [666]
g = -1

while len(total) < 10000:
    g += 1
    total += getNextGen(total, g + 3)

total = list(set(total))
total.sort()

inp = int(input())
print(total[inp - 1])