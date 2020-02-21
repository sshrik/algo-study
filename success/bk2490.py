for i in range(0, 3):
    inp = input().split(" ")
    count = 0
    for j in range(0, 4):
        if inp[j] == "0":
            count += 1
    if count == 0:
        print("E")
    elif count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    elif count == 4:
        print("D")