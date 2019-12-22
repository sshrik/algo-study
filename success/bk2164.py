import collections

N = int(input())
dq = collections.deque(range(N, 0, -1))

while len(dq) != 1:
    dq.pop()
    a = dq.pop()
    dq.appendleft(a)
print(dq[0])