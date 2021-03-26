import sys

def isContain(x, y, ox, oy, r):
    return (ox - x) ** 2 + (oy - y) ** 2 <= r ** 2

if __name__ == "__main__":
    # Test Case T
    T = int(sys.stdin.readline().rstrip())

    for _ in range(0, T):
        # Start, End - X, Y
        inp = sys.stdin.readline().rstrip().split(" ")
        stX = int(inp[0])
        stY = int(inp[1])
        enX = int(inp[2])
        enY = int(inp[3])

        # Orbit Number N
        N = int(sys.stdin.readline().rstrip())

        result = 0
        for i in range(0, N):
            inp = sys.stdin.readline().rstrip().split(" ")
            orbitX = int(inp[0])
            orbitY = int(inp[1])
            orbitR = int(inp[2])
            sContain = isContain(stX, stY, orbitX, orbitY, orbitR)
            eContain = isContain(enX, enY, orbitX, orbitY, orbitR)
            if sContain and not eContain:
                result += 1
            elif eContain and not sContain:
                result += 1
        print(result)