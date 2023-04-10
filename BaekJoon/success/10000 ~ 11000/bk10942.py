# https://www.acmicpc.net/problem/10942
import sys

fastIo = sys.stdin.readline

def isPalindrome(numArr, palindrome, S, E):
  if S > E:
    return False
  
  elif S == E:
    return True
  
  if E - S == 1:
    return numArr[S] == numArr[E]
  
  if palindrome[S + 1][E - 1] == 1:
    return numArr[S] == numArr[E]
  
  return False

if __name__ == "__main__":
  N = int(fastIo())
  numArr = list(map(int, fastIo().split()))
  
  palindrome = [[0 for _ in range(N)] for _ in range(N)]
  
  for i in range(N):
    palindrome[i][i] = 1
  
  for interval in range(0, N):
    for s in range(0, N - interval):
      if isPalindrome(numArr, palindrome, s, s + interval):
        palindrome[s][s + interval] = 1
        # print(numArr[s:s + interval + 1], "은 팰린드롬입니다.")
      else:
        palindrome[s][s + interval] = 0
        # print(numArr[s:s + interval + 1], "은 팰린드롬이 아닙니다.")
  
  M = int(fastIo())
  
  for m in range(M):
    [S, E] = list(map(int, fastIo().split()))
    
    print(palindrome[S - 1][E - 1])

'''
7
1 1 1 1 3 1 1
4
1 3
2 5
3 3
5 7
'''