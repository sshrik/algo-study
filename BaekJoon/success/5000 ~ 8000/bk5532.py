import sys
import math

if __name__ == "__main__":
    vac = int(sys.stdin.readline().rstrip())
    kor = int(sys.stdin.readline().rstrip())
    mat = int(sys.stdin.readline().rstrip())

    day_kor = int(sys.stdin.readline().rstrip())
    day_mat = int(sys.stdin.readline().rstrip())

    working = max([math.ceil(kor / day_kor), math.ceil(mat / day_mat)])
    print(vac - working)
