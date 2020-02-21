import collections

def pushFront(d, v):
    d.appendleft(v)

def pushBack(d, v):
    d.append(v)

def popFront(d):
    return d.popleft() if size(d) != 0 else -1

def popBack(d):
    return d.pop() if size(d) != 0 else -1

def size(d):
    return len(d)

def empty(d):
    return 1 if size(d) == 0 else 0

def front(d):
    return d[0] if size(d) != 0 else -1

def back(d):
    return d[-1] if size(d) != 0 else -1
            