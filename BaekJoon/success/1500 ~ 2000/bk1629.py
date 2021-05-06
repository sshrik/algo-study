#https://www.acmicpc.net/problem/1629
import sys
fastio = sys.stdin.readline

if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    A = int(inp[0])
    B = int(inp[1])
    C = int(inp[2])

    a_pow = [A]
    b_pow = [1]
    b = 1
    
    while b <= B:
        now = a_pow[-1]
        a_pow.append((now * now) % C)
        b_pow.append(b * 2)
        b = b_pow[-1]
    
    now_index = len(b_pow) - 1
    add_up_b = 0
    result = 1
    while add_up_b != B and now_index > -1:
        if b_pow[now_index] + add_up_b <= B:
            add_up_b += b_pow[now_index]
            result = (result * a_pow[now_index]) % C
        if b_pow[now_index] + add_up_b > B:
            now_index -= 1
    print(result)