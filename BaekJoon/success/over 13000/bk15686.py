import sys
from itertools import combinations

def calc_chicken_length(house_cord, chicken_cord):
    hlength = len(house_cord)
    clength = len(chicken_cord)

    # length_list[h][c] = h house and c market`s length.
    length_list = [[0  for _ in range(0, clength)] for _ in range(0, hlength)]

    for h in range(0, hlength):
        for c in range(0, clength):
            length_list[h][c] = calc_length(house_cord[h], chicken_cord[c])
    
    return length_list

def calc_length(cord1, cord2):
    return abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1])


if __name__ == "__main__":
    [N, M] = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    house_cord = []
    chicken_cord = []

    for i in range(0, N):
        inp = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        for j in range(0, N):
            if inp[j] == 1:
                house_cord.append((i, j))
            elif inp[j] == 2:
                chicken_cord.append((i, j))
    
    clength = len(chicken_cord)
    hlength = len(house_cord)
    available_chicken = list(combinations(range(0, clength), M))
    length_list = calc_chicken_length(house_cord, chicken_cord)
    
    min_length = N * N * hlength
    min_length_list = []
    for ac in available_chicken:
        length_add = 0
        min_length_list.append([])
        for h in range(0, hlength):
            min_chick = N * N
            for candidate in ac:
                if min_chick > length_list[h][candidate]:
                    min_chick = length_list[h][candidate]
            length_add += min_chick
        if min_length > length_add:
            min_length = length_add
    print(min_length)
