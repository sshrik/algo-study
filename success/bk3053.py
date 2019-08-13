import math

def euclideRound(r):
    return r * r * math.pi
def taxiRound(r):
    return 2 * r * r

inp = int(input())
print(euclideRound(inp))
print(taxiRound(inp))