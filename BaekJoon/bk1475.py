import sys


if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    N = int(sys.stdin.readline().rstrip())
    number_set = [0 for _ in range(0, 10)]

    for n in str(N):
        if n == "6" or n == "9":
            if number_set[6] < number_set[9]:
                number_set[6] += 1  
            else:
                number_set[9] += 1
        else:
            number_set[int(n)] += 1
    print(max(number_set))