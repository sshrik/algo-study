import sys

def setCheck(check, i, n):
    if check[i][n - 1]:
        check[i][n - 1] = False
        return True
    return False

def setBoxCheck(box_check, r, c, n):
    i = int(r / 3)
    j = int(c / 3)
    if box_check[i][j][n - 1]:
        box_check[i][j][n - 1] = False
        return True
    return False

def getAllowList(row_check, col_check, box_check, r, c):
    allow_list = []
    r_check = row_check[r]
    c_check = col_check[c]
    b_check = box_check[int(r / 3)][int(c / 3)]

    for ind in range(9):
        if r_check[ind] and c_check[ind] and b_check[ind]:
            # Allow when 3 check is true.
            allow_list.append(ind + 1)

    return allow_list

if __name__ == "__main__":
    sdoku_map = []

    row_check = [[True for _ in range(9)] for _ in range(9)]
    col_check = [[True for _ in range(9)] for _ in range(9)]
    box_check = [[[True for _ in range(9)] for _ in range(3)] for _ in range(3)]
    
    for r in range(9):
        sdoku_map.append([])
        inp = sys.stdin.readline().rstrip().split(" ")
        for c in range(9):
            inp_num = int(inp[c])
            sdoku_map[c].append(inp_num)
            if inp_num != 0:
                setCheck(row_check, r, inp_num) = False   # r 번째 row에 inp_num이라는 숫자가 이미 있다.
                setCheck(col_check, c, inp_num) = False   # c 번째 column에 inp_num이라는 숫자가 이미 있다.
                setBoxCheck(box_check, r, c, inp_num)   # r, c 에 위치한 3 x 3 box에 1 ~ 9 숫자가 가능한가?
    
