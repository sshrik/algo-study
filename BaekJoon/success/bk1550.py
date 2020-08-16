import sys

def hex_to_dec(num):
    hex_num = ['A', 'B', 'C', 'D', 'E', 'F']
    dec_num = [10, 11, 12, 13, 14, 15]
    if num in hex_num:
        return dec_num[hex_num.index(num)]
    else:
        return int(num)

if __name__ == "__main__":
    # For fast I / O. T mean test case number.
    inp = sys.stdin.readline().rstrip()

    power16 = [1]
    for i in range(1, len(inp)):
        power16.append(power16[i - 1] * 16)

    decimal = 0

    for i in range(0, len(inp)):
        decimal = decimal + (hex_to_dec(inp[i]) * power16[len(inp) - i - 1])
    print(decimal)