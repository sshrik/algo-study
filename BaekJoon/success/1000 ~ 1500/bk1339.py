# https://www.acmicpc.net/problem/1339
import sys

fastio = sys.stdin.readline

if __name__ == "__main__":
  N = int(fastio())
  words = [fastio().strip() for _ in range(N)]
  
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  
  alphabetValue = [[0, alphabet[i]] for i in range(26)]
  
  for word in words:
    for i in range(len(word)):
      alphabetValue[ord(word[i]) - ord('A')][0] += 10 ** (len(word) - i - 1)
    
  alphabetValue.sort(reverse=True)
  
  nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
  
  addAll = 0
  
  for i in range(10):
    if alphabetValue[i][0] != 0:
      addAll += alphabetValue[i][0] * nums[i]
  
  print(addAll)
  
  