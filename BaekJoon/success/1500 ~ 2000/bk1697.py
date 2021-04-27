# https://www.acmicpc.net/problem/1697
import sys
fastio = sys.stdin.readline
MAX_NUM = 100000 + 1

if __name__ == "__main__":
    inp = fastio().rstrip().split(" ")
    N = int(inp[0])
    K = int(inp[1])
    
    count = [MAX_NUM for i in range(MAX_NUM)]

    visit = [False for _ in range(MAX_NUM)]
    setting_queue = [N]
    count[N] = 0
    while setting_queue:
        now = setting_queue[0]
        del setting_queue[0]

        if now - 1 >= 0:
            if count[now] + 1 < count[now - 1]:
                count[now - 1] = count[now] + 1 
                setting_queue.append(now - 1)
        if now + 1 < MAX_NUM:
            if count[now] + 1 < count[now + 1]:
                count[now + 1] = count[now] + 1
                setting_queue.append(now + 1)
        if now * 2 < MAX_NUM:
            if count[now] + 1 <= count[now * 2]:
                count[now * 2] = count[now] + 1
                setting_queue.append(now * 2) 
        if count[K] != MAX_NUM:
            print(count[K])
            break
        
        