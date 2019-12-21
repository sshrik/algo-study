import sys 
import time

# Start time init for input function.
start = time.time()

for _ in range(0, 500000):
    inp = input()
    legnth = len(inp)

print("Input time : " + str(time.time() - start))

# Init for sys.stdin.
start = time.time()

for _ in range(0, 500000):
    inp = sys.stdin.readline().rstrip()
    legnth = len(inp)

print("Stdin time : " + str(time.time() - start))