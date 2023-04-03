# https://www.acmicpc.net/problem/1806
import sys

fastio = sys.stdin.readline

if __name__ == "__main__":
  [N, S] = list(map(int, fastio().split()))
  arr = list(map(int, fastio().split()))
  
  startIndex = 0
  
  sumTotal = 0
  
  result = 1000000
  
  for endIndex in range(N):
    sumTotal += arr[endIndex]
    
    if sumTotal >= S:
      while sumTotal - arr[startIndex] >= S:
        sumTotal -= arr[startIndex]
        startIndex += 1
      
      result = min(result, endIndex - startIndex + 1)     
      
  print(0 if result == 1000000 else result)
      