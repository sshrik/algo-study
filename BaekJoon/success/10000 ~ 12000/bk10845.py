# Make Queue
import sys

def push(x, q):
    q.append(x)

def pop(q):
    if len(q) == 0:
        return -1
    else:
        result = q[0]
        del q[0]
        return result

def front(q):
    return q[0] if len(q) != 0 else -1

def back(q):
    return q[-1] if len(q) != 0 else -1

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    q = []
    size = 0
    for _ in range(0, n):
        inp = sys.stdin.readline().rstrip()
        if " " in inp:
            push(int(inp.split(" ")[1]), q)
            size += 1
        elif inp[0] == 'p':
            if size == 0:
                print("-1")
            else:
                print(pop(q))
                size -= 1
        elif inp[0] == 's':
            print(size)
        elif inp[0] == 'e':
            print(1 if size == 0 else 0)
        elif inp[0] == 'f':
            print(front(q))
        elif inp[0] == 'b':
            print(back(q))