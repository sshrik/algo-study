# https://www.acmicpc.net/problem/10816
import sys
fastio = sys.stdin.readline

def makeTreeValue(value):
    return [value, 1, None, None]

def bst_add(tree, value):
    if tree == None:
        return makeTreeValue(value)

    now = tree
    while True:
        if now[0] == value:
            now[1] += 1
            break
        elif now[0] > value:
            if now[2] == None:
                now[2] = makeTreeValue(value)
                break
            else:
                now = now[2]
        else:
            if now[3] == None:
                now[3] = makeTreeValue(value)
                break
            else:
                now = now[3]
    return tree

def bst_search(tree, value):
    if tree == None:
        return -1

    now = tree
    while True:
        if now[0] == value:
            return now[1]
        elif now[0] > value:
            if now[2] == None:
                return -1
            else:
                now = now[2]
        else:
            if now[3] == None:
                return -1
            else:
                now = now[3]


if __name__ == "__main__":
    N = int(fastio().rstrip())
    tree = None
    inp = fastio().rstrip().split(" ")
    for i in inp:
        tree = bst_add(tree, int(i))
  
    M = int(fastio().rstrip())

    inp = fastio().rstrip().split(" ")
    for i in inp:
        dst = bst_search(tree, int(i))
        if dst == -1:
            dst = 0
        print(dst, end=" ")

