import math
inp = input()

a = int(inp.split(" ")[0])
b = int(inp.split(" ")[1])
v = int(inp.split(" ")[2])

'''
( a - b ) * ( x  - 1) + a > v

v - a / a - b < x - 1

a - b * x - 1 < v < a - b * x - 1 + a
'''

print(math.ceil((v - a) / (a - b)) + 1)
