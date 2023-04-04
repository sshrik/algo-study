# https://www.acmicpc.net/problem/7579
import sys

fastio = sys.stdin.readline

MAX_COST = 10000

if __name__ == "__main__":
  [N, M] = list(map(int, fastio().split()))
  memory = list(map(int, fastio().split()))
  cost = list(map(int, fastio().split()))
  
  result = [0 for _ in range(MAX_COST + 1)]
  
  for n in range(N):
    for c in range(MAX_COST, -1, -1):
      if c - cost[n] >= 0:
        result[c] = max(result[c], result[c - cost[n]] + memory[n])
    
  minValue = MAX_COST + 1
      
  for c in range(MAX_COST + 1):
    if result[c] >= M:
      minValue = min(minValue, c)

  print(minValue)