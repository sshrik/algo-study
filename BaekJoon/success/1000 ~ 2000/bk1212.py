import sys

if __name__ == "__main__":
    non_zero_e_to_t = ["0", "1", "10", "11", "100", "101", "110", "111"]
    e_to_t = ["000", "001", "010", "011", "100", "101", "110", "111"]
    digit_8 = sys.stdin.readline().rstrip()

    ans = ""
    for i in range(0, len(digit_8)):
        if i == 0:
            ans += non_zero_e_to_t[int(digit_8[i])]
        else:
            ans += e_to_t[int(digit_8[i])]
    print(ans)