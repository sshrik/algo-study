import collections
import sys 


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


if __name__ == "__main__":
    N = int(input())
    deck = collections.deque()
    for _ in range(0, N):
        inp = sys.stdin.readline().rstrip().split(" ")
        if inp[0] == "push_back":
            pushBack(deck, int(inp[1]))
        elif inp[0] == "push_front":
            pushFront(deck, int(inp[1]))
        elif inp[0] == "pop_back":
            print(popBack(deck))
        elif inp[0] == "pop_front":
            print(popFront(deck))
        elif inp[0] == "size":
            print(size(deck))
        elif inp[0] == "empty":
            print(empty(deck))
        elif inp[0] == "front":
            print(front(deck))
        elif inp[0] == "back":
            print(back(deck))
            