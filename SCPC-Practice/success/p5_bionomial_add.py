import sys

NUM_MAX = 1000000007
INDEX_MAX = 1000000

def set_factorial(max_size):
    # Will be return [0!, 1!, ... , max_size!]
    ret_list = [1]
    size = 1

    while size < max_size + 1:
        ret_list.append((ret_list[-1] * size) % NUM_MAX)
        size += 1
    
    return ret_list

def get_mod_power(num, power):
    rem = 1

    while power > 0:
        if power % 2 != 0:
            rem = (rem * num) % NUM_MAX
        num = (num * num) % NUM_MAX
        power = int(power/2) if power % 2 == 0 else int((power-1)/2)

    return rem

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    T = int(sys.stdin.readline().rstrip())
    factorial = set_factorial(INDEX_MAX + INDEX_MAX + 2)

    for t in range(0, T):
        inp = sys.stdin.readline().rstrip().split(" ")
        N = int(inp[0])
        M = int(inp[1])

        power_value = get_mod_power((factorial[M+1] * factorial[N+1]) % NUM_MAX, NUM_MAX - 2)
        answer = (factorial[M+N+2] * power_value - 1) % NUM_MAX

        print("Case #" + str(t + 1))
        print(answer)

