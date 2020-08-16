import sys

DOWN = 0
UP = 1

def get_miro_val(x, y, N):
    n = x + y
    # 윗 삼각형
    if N % 2 == 0:
        if n <= N:
            if n % 2 != 0:
                return int((n + 1) * n / 2) + y + 1
            else:
                return int((n + 1) * n / 2) + x + 1
        # 아랫 삼각형
        else:
            if n % 2 != 0:
                return int(n * (n + 1) / 2) + y
            else:
                return int(n * (n + 1) / 2) + x
    else:
        if n <= N:
            if n % 2 != 0:
                return int((n + 1) * n / 2) + x + 1
            else:
                return int((n + 1) * n / 2) + y + 1
        # 아랫 삼각형
        else:
            if n % 2 != 0:
                return int(n * (n + 1) / 2) + x
            else:
                return int(n * (n + 1) / 2) + y


def set_x(x, move):
    if move == "U":
        return x - 1
    elif move == "D":
        return x + 1
    else:
        return x
        
def set_y(y, move):
    if move == "L":
        return y - 1
    elif move == "R":
        return y + 1
    else:
        return y
    
if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    T = int(sys.stdin.readline().rstrip())
    for t in range(0, T):
        inp = sys.stdin.readline().rstrip().split(" ")
        N = int(inp[0])
        K = int(inp[1])

        for i in range(0, N):
            for j in range(0, N):
                print(get_miro_val(i, j, N), end=" ")
            print()

        moving = sys.stdin.readline().rstrip()
        x = 0
        y = 0
        answer = get_miro_val(x, y, N)

        for move in range(0, K):
            x = set_x(x, moving[move])
            y = set_y(y, moving[move])
            answer += get_miro_val(x, y, N)
        
        print("Case #" + str(t + 1))
        print(answer)
