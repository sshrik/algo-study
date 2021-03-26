import sys

if __name__ == "__main__":
    inp = sys.stdin.readline().rstrip().split(" ")
    A = int(inp[0]) # 0 ~ 23
    B = int(inp[1]) # 0 ~ 59
    C = int(sys.stdin.readline().rstrip())

    A = (A + (C // 60) + (( B + (C % 60) ) // 60 )) % 24
    B = (B + (C % 60)) % 60
    print(str(A) + " " + str(B)) 
