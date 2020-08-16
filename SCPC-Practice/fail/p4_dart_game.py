import sys
import math

# Setting of score board.
BULL = -1
SINGLE = 1
DOUBLE = 2
TRIPLE = 3
OUT = 0

# Score stating from x axis.
score_board = [6, 13, 4, 18, 1, 20, 5, 12, 9, 14, 11, 8, 16, 7, 19, 3, 17, 2, 15, 10]
score_incli = [math.tan(math.radians(-9 + (18 * i))) for i in range(0, 11)]
R_NUMBER = 5

def get_score(x, y, r_list):
    r_power = [r_list[i] * r_list[i] for i in range(0, R_NUMBER)]
    kind = get_score_kind(x, y, r_power)
    if kind == OUT:
        return 0
    elif kind == BULL:
        return 50
    else:
        try:
            return get_partial_score(x, y) * kind
        except:
            print(y / x)
            print(score_incli)
        

def get_score_kind(x, y, r_list):
    length = x * x + y * y  # Length from (0, 0) to (x, y)

    if length < r_list[0]:
        return BULL
    elif length > r_list[1] and length < r_list[2]:
        return TRIPLE
    elif length > r_list[3] and length < r_list[4]:
        return DOUBLE
    elif length > r_list[4]:
        return OUT
    else:
        return SINGLE

def get_partial_score(x, y):
    if x == 0:
        return 20 if y > 0 else 3
    elif y == 0:
        return 6 if x > 0 else 11
    else:
        problem_incli = y / x
        if score_incli[0] < problem_incli and problem_incli < 0:
            return score_board[0] if x > 0 else score_board[0 + 10]
        if score_incli[1] > problem_incli and problem_incli > 0:
            return score_board[0] if x > 0 else score_board[0 + 10]
        for i in range(1, 5):
            if score_incli[i] < problem_incli and problem_incli < score_incli[i + 1]:
                return score_board[i] if x > 0 else score_board[i + 10]
        if score_incli[5] < problem_incli:
            return score_board[5] if x > 0 else score_board[5 + 10]
        if score_incli[6] > problem_incli:
            return score_board[5] if x > 0 else score_board[5 + 10]
        for i in range(6, 10):
            if score_incli[i] < problem_incli and problem_incli < score_incli[i + 1]:
                return score_board[i] if x < 0 else score_board[i + 10]
        
if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())  # For fast I / O. T mean test case number.
    for t in range(0, T):
        # Init values.
        inp = sys.stdin.readline().rstrip().split(" ")
        r_list = [int(inp[i]) for i in range(0, R_NUMBER)]

        N = int(sys.stdin.readline().rstrip())
        total_score = 0
        
        for i in range(-30000, 30000):
            for j in range(-30000, 30000):
                get_score(i, j, r_list)

        '''
        for _ in range(0, N):
            inp = sys.stdin.readline().rstrip().split(" ")
            total_score += get_score(int(inp[0]), int(inp[1]), r_list)
        '''

        print("Case #" + str(t + 1))
        print(total_score)