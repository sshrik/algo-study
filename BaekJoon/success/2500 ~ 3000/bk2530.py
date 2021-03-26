import sys

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    H = int(inp[0]) # 0 ~ 23
    M = int(inp[1]) # 0 ~ 59
    S = int(inp[2]) # 0 ~ 59

    add = int(sys.stdin.readline().rstrip())

    S = S + (add % 60)
    if S >= 60:
        M += (S // 60)
    S = S % 60

    add = add // 60

    M = M + (add % 60)
    if M >= 60:
        H += (M // 60)
    M = M % 60
    
    add = add // 60

    H = H + (add % 24)
    H = H % 24

    print(str(H) + " " + str(M) + " " + str(S)) 
