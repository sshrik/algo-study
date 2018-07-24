x = input()
l = x.split(" ")

wordNum = 0

for i in range(0, len(l)):
    if len(l[i]) != 0:
        wordNum += 1
print(wordNum)
