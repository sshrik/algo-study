# https://www.acmicpc.net/problem/14890
import sys

def can_go(map_arr, n, l):
    before = map_arr[0]
    using = [False] * n

    a = 0
    while a < n:
        # print(a, map_arr, using)
        if before == map_arr[a]:
            before = map_arr[a]
        elif before + 1 == map_arr[a]:
            if a - l < 0:
                return False
            first = map_arr[a - l]
            for i in range(a - l, a):
                if first != map_arr[i] or using[i]:
                    return False
            for i in range(a - l, a):
                using[i] = True
            before = map_arr[a]
        elif before - 1 == map_arr[a]:
            if a + l > n:
                return False
            first = map_arr[a]
            for i in range(a, a + l):
                if first != map_arr[i] or using[i]:
                    return False
            for i in range(a, a + l):
                using[i] = True
            a += l - 1
            before = map_arr[a]
        else:
            return False

        a += 1
    return True


if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    n = int(inp[0])
    l = int(inp[1])

    map_info = []
    for _ in range(n):
        inp = sys.stdin.readline().rstrip().split(" ")
        map_info.append([])
        for i in inp:
            map_info[-1].append(int(i))
    
    count = 0
    for i in range(n):
        if can_go(map_info[i], n, l):
            # print("Row ", i, map_info[i])
            count += 1
        temp = []
        for j in range(n):
            temp.append(map_info[j][i])
        if can_go(temp, n, l):
            # print("Column ", i, temp)
            count += 1
    
    print(count)

    # print(can_go([3, 3, 2, 1, 1, 1], 6, 2))