import sys

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    min_burger = 2001
    for _ in range(0, 3):
        burger = int(sys.stdin.readline().rstrip())
        if burger < min_burger:
            min_burger = burger
    
    min_soda = 2001
    for _ in range(0, 2):
        soda = int(sys.stdin.readline().rstrip())
        if soda < min_soda:
            min_soda = soda

    print(min_soda + min_burger - 50)