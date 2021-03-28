# https://www.acmicpc.net/problem/11758
def ccw(p1, p2, p3):
    a = (p2[0] - p1[0], p2[1] - p1[1])
    b = (p3[0] - p1[0], p3[1] - p1[1])
    return a[0] * b[1] - b[0] * a[1]

if __name__ == "__main__":
    p = []
    for _ in range(3):
        inp = input().split(" ")
        p.append((int(inp[0]), int(inp[1])))
    
    D = ccw(p[0], p[1], p[2])
    if D < 0:
        print("-1")
    elif D == 0:
        print("0")
    else:
        print("1")