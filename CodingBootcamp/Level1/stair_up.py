# n 개의 계단을 오를 때 총 몇가지 방법으로 오를 수 있는가?
# n 은 1 에서 45 사이, 2 -> 2, 3 -> 3

import sys

n = sys.stdin.readline().rstrip()
dp = [0 for _ in range(0, 46)]
dp[1] = 1
dp[2] = 2

for i in range(3, 46):
    # 1계단 전은 1번 걸어 오면 되고, 2계단 전에서는 2계단 오르면 됨.
    dp[i] = dp[i - 1] + dp[i - 2] # 각각 더해서 45 까지 구함.

print(dp[n])